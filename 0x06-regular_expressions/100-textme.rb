#!/usr/bin/env ruby
ARGV[0].scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/) { |match| puts match.join(",") }

