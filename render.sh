#!/usr/bin/env bash
# Renders every scene listed below into frontend/public/videos/.
# Usage: ./render.sh        (720p30)
#        ./render.sh -qh    (pass a different manim quality flag)
set -euo pipefail
cd "$(dirname "$0")"

QUALITY="${1:--qm}"
OUT=frontend/public/videos
TMP=$(mktemp -d)
mkdir -p "$OUT"

# "<python file> <SceneClass>" — add a line here for each new algorithm
SCENES=(
  "algorithms/linear_search.py LinearSearch"
  "algorithms/binary_search.py BinarySearch"
  "algorithms/bubble_sort.py BubbleSort"
  "algorithms/linked_list.py LinkedListTraversal"
)

for entry in "${SCENES[@]}"; do
  read -r file scene <<<"$entry"
  venv/bin/manim "$QUALITY" --media_dir "$TMP" "$file" "$scene"
  find "$TMP/videos" -name "$scene.mp4" -not -path "*partial_movie_files*" -exec cp {} "$OUT/$scene.mp4" \;
done

rm -rf "$TMP"
echo "Rendered videos into $OUT"
