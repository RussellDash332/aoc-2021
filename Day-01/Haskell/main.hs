import System.IO

-- Converts string to integer
toInt:: String -> Int
toInt = read

-- Part 1 and 2 combined
count :: [String] -> Int -> Int
count inputs start = ans where
    check ans idx =
        ans + fromEnum (toInt (inputs !! idx) > toInt (inputs !! (idx - start)))
    ans = foldl check 0 [start..length inputs - 1]

main = do
  contents <- readFile "../01.in"
  let inputs = lines contents
  putStr "Part 1: "; print (count inputs 1)
  putStr "Part 2: "; print (count inputs 3)