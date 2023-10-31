#!/usr/bin/env ruby

argument = ARGV[0]
if not argument
    puts "Insert an argument to look for matching expressions"
else
    puts argument.scan(/\Ah[a-zA-Z0-9]*n\Z/).join
end
