library(stringr)
library(tidyverse)

all_words <- read.csv("word_lists/english_words.csv")

five_letter_words <- all_words %>% 
  filter(str_length(word) == 5)

frequent_words <- five_letter_words %>% 
  filter(freq >= 1550)

five_letter_words %>% 
  select(word) %>% 
  write_csv("word_lists/valid_guesses.csv")

frequent_words %>% 
  select(word) %>% 
  write_csv("word_lists/valid_solutions.csv")
