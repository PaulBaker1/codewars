# Nushell script to count solutions by difficulty and language
# and update badges in README.md.
# Usage: nu scripts/update_readme.nu

let root = (pwd)
let readme_path = $"($root)/README.md"
let diffs = ["8-kyu" "7-kyu" "6-kyu" "5-kyu" "4-kyu" "3-kyu" "2-kyu" "1-kyu"]
let lang_badge_labels = ["Python" "JavaScript" "Java" "TypeScript" "Go" "CSharp" "Kotlin"]

mut counts_by_diff = ($diffs | reduce -f {} {|d acc| $acc | upsert $d 0 })
mut counts_by_lang = {}
mut total = 0

for d in $diffs {
  if ($d | path exists) {
    let lang_dirs = (ls $d | where type == dir | get name)
    for lang_dir in $lang_dirs {
      let lang = ($lang_dir | path basename | str downcase)

      # recursive: use glob pattern
      let files = (ls $"($lang_dir)/**" | where type == file | where name !~ '\.md$')

      for f in $files {
        $total = ($total + 1)
        $counts_by_diff = ($counts_by_diff | update $d ( ($counts_by_diff | get $d) + 1 ))
        if ($counts_by_lang | columns | any {|c| $c == $lang }) {
          $counts_by_lang = ($counts_by_lang | update $lang ( ($counts_by_lang | get $lang) + 1 ))
        } else {
          $counts_by_lang = ($counts_by_lang | upsert $lang 1)
        }
      }
    }
  }
}


# Helper: patch one badge in text using regex (replaces all occurrences for that label)
def patch-badge [text label value:int] {
  let pattern = $'!\[.*?\]\(https://img\.shields\.io/badge/($label)-\d+-(.+?)\)'
  let repl = $'![($label)](https://img.shields.io/badge/($label)-($value)-$1)'
  $text | str replace -r $pattern $repl
}

# Read README, patch badges
mut readme = (open --raw $readme_path)

$readme = (patch-badge $readme "solved" $total)

for d in $diffs {
  let label = ($d | str replace "-" "_")
  let val = ($counts_by_diff | get $d)
  $readme = (patch-badge $readme $label $val)
}

for lbl in $lang_badge_labels {
  let key = ($lbl | str downcase)
  let val = (if ($counts_by_lang | columns | any {|c| $c == $key }) { $counts_by_lang | get $key } else { 0 })
  $readme = (patch-badge $readme $lbl $val)
}

$readme | save -f $readme_path
print $"Updated README: total=($total), by_diff=($counts_by_diff), by_lang=($counts_by_lang)"
