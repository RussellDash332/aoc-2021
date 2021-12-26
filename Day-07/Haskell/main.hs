import System.IO
import Data.List (sort)

-- Converts string to integer
toInt:: String -> Int
toInt = read

-- https://stackoverflow.com/questions/4978578/how-to-split-a-string-in-haskell
wordsWhen     :: (Char -> Bool) -> String -> [String]
wordsWhen p s =  case dropWhile p s of
                      "" -> []
                      s' -> w : wordsWhen p s''
                            where (w, s'') = break p s'

-- Part 1
p1 :: [Int] -> Int
p1 inputs = ans where
    go ans inp = ans + abs (inp - inputs !! (length inputs `div` 2))
    ans = foldl go 0 inputs

-- Part 2
p2 :: [Int] -> Int
p2 inputs = ans where
    add ans inp = ans + inp
    mean = foldl add 0 inputs `div` length inputs
    go ans inp = ans + (abs(inp - mean) * (abs(inp - mean) + 1)) `div` 2
    ans = foldl go 0 inputs

main = do
  contents <- readFile "../07.in"
  let inputs = sort (map (toInt) (wordsWhen (==',') contents))

  putStr "Part 1: "; print (p1 inputs)
  putStr "Part 2: "; print (p2 inputs)