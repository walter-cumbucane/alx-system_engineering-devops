#!/usr/bin/env ruby

argument = ARGV[0]
if not argument
    puts "Insert an argument to look for matching expressions"
else
    puts argument.scan(/hb+tn/).join
end
