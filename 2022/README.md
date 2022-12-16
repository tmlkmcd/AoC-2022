## Day 1

- Estimated completion time: ~3 minutes

Easy peasy. Got snagged for a minute on parsing the empty line between each elf which was a bit silly.

## Day 2

- Estimated completion time: ~20 minutes

Hard-coding ftw. Fumbled a lot on trying to figure out a more dynamic strategy before deciding to simply hard-code everything. I'm TOO TIRED!!

## Day 3

- Estimated completion time: ~15 minutes

Spent a long time fumbling over part 1 because I wasn't sure if I had understood the question correctly (unique duplicates or just all duplicates?) - my solution kept coming up with a number that was way too high then randomly output the right answer without any change on my part that I knew of. Part 2 went down on the first try (about 2 minutes) which is atypical for me.

## Day 4

- Estimated completion time: ~15 minutes

This 5am thing is really biting me. Trying to get the logic right when I can barely think is a bit of a monster...

## Day 5

- Estimated completion time: ~30 minutes

As ever, long time deciding how to parse input in a half-asleep haze. Though each step of the way lots of debugging and figuring out but it did go down smoothly. Getting harder but still fun.

## Day 6

- Estimated completion time: ~15 minutes

Surprisingly easy that we're near a week into the challenge, should have finished a lot faster but got snagged on the looping/deduping logic which I think I'd have done much faster in JavaScript. It being 5am still doesn't help...

Also, didn't know about sets in python / that they were that similar to JS. This is how we learn!!

## Day 7

- Estimated completion time: ~35 minutes

First trickier one of the year and great fun. Object-oriented programming ftw. Had a full night's sleep last night - the right choice, I'd never have been able to do this one groggy...

## Day 8

- Estimated completion time: ~70 minutes

Tough one today. Both parts there was trouble getting the looping logic correct, part 2 I had trouble with because I misread the brief a few times before implementing it correctly.

## Day 9

- Estimated completion time: ~90 minutes

Much of the delay was implementing the 'snapping' logic when a 'tail' piece has to move diagonally (and implementing various visualisations before I realised that was what the bug was).

#### Forgot to update for a few days...

Last time I was on a train in mainland Europe doing [Advent of Code](https://adventofcode.com/2019/day/13) I was [playing breakout](https://github.com/tmlkmcd/AoC-2019/commit/3845d1b5b20cc2cded70ea0cf9d1ff9f3ae00a11) on an intcode computer...

## Day 10

- Estimated completion time: ~45 minutes 

Didn't complete this on the actual day due to illness. Most of the delay came from trying to figure out what the problem actually meant (both parts) with the TV on (but how good is The Office, right??). Initially tried to implement as a simply line loop that increments the step by 2 (but needs to double up the code for each cycle for the 'addx' command). Decided this wouldn't work for part 2, tried rebuilding it as a per-cycle loop but wasn't sure of a clean way to increment the register so went back to the first solution.

Ended up with a bug that meant certain pixels were missing in part 2 so I couldn't read the message. After some tinkering about, it seemed to fix itself and I'm not sure what I had wrong to begin with...🤷

## Day 11

- Estimated completion time: ~30 minutes

OOP for the win again. Had a little trouble implementing the 'keep away' logic correctly, mostly - as ever - because my knowledge of the nuances of python are holding me back a little but otherwise it works well enough. Caught onto the 'trick' for part 2 quite quickly, reminded me of another similar problem a few [years ago](https://adventofcode.com/2020/day/13). 

## Day 12

- Estimated completion time: ~30 minutes

Thankfully learned Dijkstra's as a [solution](https://github.com/tmlkmcd/AoC-2021/blob/master/day15/sol-2.py) to one of [last year's problems](https://adventofcode.com/2021/day/15), got a little stuck implementing it in a way that wasn't causing the 'pointer' to simply run around the map in circles but got there in the end.

Part 2 came quite easily once I figured out it was blowing the recursion limit because not all potential starting points can even reach the end, brute-forcing the solution was a bit of a cheat - I'd prefer to have a method that automagically eliminates unnecessary starting points if another successful path already has shown there to be a closer 'a', but the original pathfinding solution was fast enough that this was actually viable.

## Day 13

- Estimated completion time: ~20 minutes

Surprised at how quickly this one went down. Misread the problem at the start so implemented the solution slightly wrong but the correction was easy to make. Part 2 as easy as implementing a sorting function.

## Day 14

- Estimated completion time: ~35 minutes

Given how much the [similar](https://adventofcode.com/2018/day/17) problem put me off a few years ago (especially considering I was doing that year in GoLang), surprised at how quickly this one went down too. I must be getting better.

## Day 15

- Estimated completion time: ~60 minutes

Got snagged for way too long not realising that my regex was not parsing negative numbers and giving me too low an output for pt 1. Worked pretty quickly once I fixed that.

Part 2 decided to see if a library existed for merging ranges instead of simply doing it manually (low and behold, there was something). Feels a bit cheap to still brute-force my way through all y-coordinates to find the right one but definitely much faster than cycling through every coordinate manually. Takes a long time to run when scanning 4 million by 4 million points but I guess this is perhaps the quickest that could be expected 🤷 I'm not fussed about implementing sub-optimal solutions whilst I'm on holiday...

## Day 16

- Estimated completion time: ~150 minutes

By far the hardest exercise for AoC this year (so far...?). Still not even 100% sure that my answer would work for all inputs but it got me the stars so I'm happy, plus I have the extra hours while the gf is napping (still on holiday here)...

Both parts run pretty quickly on the test input but with the puzzle input, part 2 took about 5 minutes to complete.