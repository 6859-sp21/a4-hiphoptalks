# a4-hiphoptalks
a4-hiphoptalks created by Yodahe Alemu and Joshua Verdejo

**A rationale for your design decisions.** _How did you choose your particular visual encodings, interaction, and animation techniques? What alternatives did you consider and how did you arrive at your ultimate choices?_

The core of our visualization is the grid of rappers in the middle of the screen (placed there because it should be the viewer's main focus). The rappers were placed in a grid because we felt that this was the most efficient way to show all 100 of the rappers on screen without the data getting hard to read and understand. To the left of the main grid, a key card shows the current rapper that a user is hovering over along with that rapper's picture as well as the number of times they've used the word in question.

The main interactive component of our visualization is the ability to type in a word at the top of the screen. If the word a user types is in our dataset of the top 1500 words used by our rappers, then each of the rappers in the grid will grow or shrink to represent how much they use that word in comparison to the other rappers. We made sure that rappers both GROW and SHRINK from their default scale, as opposed to just SHRINKING in order to make it clear to the users which artists were using the word more than average. Users can also click on the ranked words list (ranked in order of highest used word to lowest used) on the right of the screen to see which artists have used that word in their songs. The typing interaction creates a pretty fun and exploratory system for discovering which words to use, but the word rankings gives the user insight into our dataset that the normal typing couldn't.

Originally, each rapper was placed on their own line and were represented as a svg circle filled with the artist's profile picture. In order to show how much an artist used a word, their respective circle would move along the line. We ended up moving away from this because trying to fit 100 separate lines on screen, stacked top-to-bottom, would either take up too much space (users would have to scroll to see the visualization) or the circles would have to be so small that users couldn't see which circle represented which artist. From there, we transitioned to the grid and also switched from svg circles to simple pictures since filling svgs with a background image is a lot more expensive for d3 and was causing us problems.



**An overview of your development process.** _Describe how the work was split among the team members. Include a commentary on the development process, including answers to the following questions: Roughly how much time did you spend developing your application (in people-hours)? What aspects took the most time?_

We had two team members and decided to split the development process in half. We discussed and designed the visualization together, as well as a method to scrape data, however, when it came to the actual technical implementation - one of us focused on scraping the web and generating our dataset, and one of us focused on implementing that dataset into an interactive visualization. 

Joshua handled the dataset generation. Initial attempts were done to scrape an AZLyrics website using a python library, however, AZLyrics implements a rigorous check for requests, so only 10-20 songs could be scraped per day. With the given timeframe, we realized it would be cutting the implementation a bit close. Because of this, we pivoted to the Genius API, which allows for scraping by artist instead of individual song. This allowed us to scrape 10-20 artists every few hours instead, and there were no hard restrictions on quantity of requests. After scraping the data, the data was cleaned using Beautiful Soup, parsed, and put into CSVs. Finally, the csv information was combined, and the pictures on the website were selected and downloaded by hand.

Yodahe handled the d3 implementation. Setting up a simple website with D3 took almost no time at all, and getting the csv files generated by Joshua into our site was luckily very simple because of the "d3.csv" function. The biggest issues that took the most time were 1) figuring out how to visualize 100 different artists on the screen in an efficient way and 2) figuring out how to use images for each of those artists without having the d3 animations slow down or stutter. 
