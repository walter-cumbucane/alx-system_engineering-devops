#!/usr/bin/env ruby
require "oniguruma"

regex = Oniguruma::ORegexp.new("/School/")
argument = ARGV[1]
match_data = regex.match(argument)
if match_data
    puts "#{match_data}"
end
