#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$ROOT"
ROOT_ESCAPED="$(printf '%s\n' "$ROOT" | sed -e 's/[.[\*^$()+?{|]/\\&/g' -e 's#/#\\/#g')"

upper() {
  echo "$1" | tr '[:lower:]' '[:upper:]'
}

titleize() {
  echo "$1" | sed -E 's/[-_]+/ /g' | awk '{for(i=1;i<=NF;i++){ $i=toupper(substr($i,1,1)) tolower(substr($i,2)) } print}'
}

label_from_key() {
  local key="$1"
  if [[ "$key" =~ ^ejercicio-([0-9]+([.-][0-9]+)*)$ ]]; then
    echo "Ejercicio ${BASH_REMATCH[1]}"
    return
  fi

  if [[ "$key" =~ ^segunda-parte-ejercicio-([0-9]+)$ ]]; then
    echo "Segunda Parte Ejercicio ${BASH_REMATCH[1]}"
    return
  fi

  echo "$(titleize "$key")"
}

label_from_section() {
  local section="$1"
  local base
  base="$(basename "$section")"

  if [[ "$base" =~ ^practico-([0-9]+)$ ]]; then
    echo "Practico ${BASH_REMATCH[1]}"
    return
  fi

  if [[ "$base" =~ ^teoria-([0-9]+)$ ]]; then
    echo "Teoria ${BASH_REMATCH[1]}"
    return
  fi

  echo "$(titleize "$base")"
}

rewrite_links() {
  sed -E \
    -e 's#\((\./)?README\.md\)#(./)#g' \
    -e 's#\((\./)?readme\.md\)#(./)#g' \
    -e 's#\((\./)?README-([^)]+)\.md\)#(./\2/)#g' \
    -e 's#\((\./)?readme-([^)]+)\.md\)#(./\2/)#g' \
    -e "s#\\[([^]]+)\\]\\($ROOT_ESCAPED/([^)]+)\\)#\\1 (\\2)#g"
}

normalize_math_delimiters() {
  awk '
    BEGIN { in_code = 0 }
    /^```/ {
      in_code = !in_code;
      print;
      next;
    }
    {
      if (!in_code) {
        gsub(/\\\[/, "$$");
        gsub(/\\\]/, "$$");
        gsub(/\\\(/, "$");
        gsub(/\\\)/, "$");
      }
      print;
    }
  '
}

sections_file="$(mktemp)"
{
  find practicos -mindepth 1 -maxdepth 1 -type d 2>/dev/null || true
  find . -mindepth 1 -maxdepth 1 -type d -name 'teoria-*' 2>/dev/null || true
} | sed 's#^\./##' | sort -V > "$sections_file"

if [ ! -s "$sections_file" ]; then
  rm -f "$sections_file"
  echo "No se encontraron secciones para documentar (esperado: practicos/practico-* o teoria-*)." >&2
  exit 1
fi

rm -rf docs
rm -rf static/pdfs
mkdir -p docs static/pdfs

while IFS= read -r section; do
  [ -z "$section" ] && continue

  section_label="$(label_from_section "$section")"
  section_index="docs/$section/index.md"
  section_slug="/$section/"

  mkdir -p "$(dirname "$section_index")"

  {
    echo "---"
    echo "title: \"$section_label\""
    echo "sidebar_position: 1"
    echo "slug: \"$section_slug\""
    echo "description: \"Indice de documentacion para $section\""
    echo "---"
    echo
    if [ -f "$section/README.md" ]; then
      rewrite_links < "$section/README.md" | normalize_math_delimiters
    else
      echo "# $section_label"
      echo
      echo "No se encontro un README principal en \\`$section\\`."
    fi
  } > "$section_index"

  pos=2
  while IFS= read -r src; do
    [ -z "$src" ] && continue

    base="$(basename "$src")"
    key="${base%.md}"
    key="${key#README-}"

    title="$(label_from_key "$key")"
    dest="docs/$section/$key/index.md"
    slug="/$section/$key/"

    mkdir -p "$(dirname "$dest")"

    {
      echo "---"
      echo "title: \"$title\""
      echo "sidebar_position: $pos"
      echo "slug: \"$slug\""
      echo "description: \"Contenido importado desde $src\""
      echo "---"
      echo
      rewrite_links < "$src" | normalize_math_delimiters
    } > "$dest"

    pos=$((pos + 1))
  done < <(find "$section" -maxdepth 1 -type f -name 'README-*.md' | sort -V)

  subdocs="$(find "docs/$section" -type f -name 'index.md' ! -path "$section_index" | sort -V || true)"
  if [ -n "$subdocs" ] && ! grep -q '^## Navegacion interna$' "$section_index"; then
    {
      echo
      echo "## Navegacion interna"
      echo
      echo "$subdocs" | while IFS= read -r d; do
        [ -z "$d" ] && continue
        rel="${d#docs/$section/}"
        rel="${rel%/index.md}"
        key="$(basename "$rel")"
        label="$(label_from_key "$key")"
        echo "- [$label](./$rel/)"
      done
    } >> "$section_index"
  fi

  pdfs="$(find "$section" -type f -iname '*.pdf' | sort -V || true)"
  if [ -n "$pdfs" ]; then
    {
      echo
      echo "## Material PDF"
      echo
      echo "$pdfs" | while IFS= read -r pdf; do
        [ -z "$pdf" ] && continue
        rel="${pdf#./}"
        mkdir -p "static/pdfs/$(dirname "$rel")"
        cp "$pdf" "static/pdfs/$rel"
        name="$(basename "$pdf")"
        echo "- [$name](/pdfs/$rel)"
      done
    } >> "$section_index"
  fi
done < "$sections_file"

cat > docs/intro.md <<'INTRO'
---
title: "Documentacion"
sidebar_position: 1
slug: "/"
description: "Indice principal de documentacion"
---

# Documentacion

Documentacion consolidada de computabilidad y complejidad.

## Secciones
INTRO

while IFS= read -r section; do
  [ -z "$section" ] && continue
  label="$(label_from_section "$section")"
  echo "- [$label](./$section/)" >> docs/intro.md
done < "$sections_file"

root_pdfs="$(find . -maxdepth 1 -type f -iname '*.pdf' | sort -V || true)"
if [ -n "$root_pdfs" ]; then
  {
    echo
    echo "## Material General PDF"
    echo
    echo "$root_pdfs" | while IFS= read -r pdf; do
      [ -z "$pdf" ] && continue
      rel="${pdf#./}"
      mkdir -p "static/pdfs"
      cp "$pdf" "static/pdfs/$rel"
      name="$(basename "$pdf")"
      echo "- [$name](/pdfs/$rel)"
    done
  } >> docs/intro.md
fi

rm -f "$sections_file"
echo "Documentacion regenerada en docs/ y static/pdfs/."
