---
geometry: margin=1in
pdf-engine: pdflatex
---

# Part I - Global Population 
The goal of this section is to explore global changes in the population of the United States. 
The U.S. Census Bureau maintains a file (popclockest.txt) containing national population estimates between 1900 and 1999. 
Import this data set into MATLAB or EXCEL (right click to save the file as text). Then answer the following questions.     

1. Plot the U.S. population as a function of time. What do you conclude?    
2. Can the growth of the U.S. population be modeled by a simple evolution equation of the form $(N(t+1) = (1 + R) N(t)$, where $t$ is in years? Why or why not? If so, find an estimate of $R$.     
3. Post-census population estimates are obtained as described on the U.S. Census Bureau methodology page (see for instance the [methodology file for the 2022 vintage](./global_pop/methods-statement-v2022.pdf). Explain the main formula given in the Overview section of this article.     
4. Given the following estimates (downloaded in 2005 from a now decommissioned US Census Bureau page), find the population of the U.S. in 2004.         
    a. Population in 2001: 285,102,075.         
    b. Births, deaths, and net international immigration:             
        + 2001-2002: 4,006,985; 2,429,999; 1,262,159.             
        + 2002-2003: 4,055,469; 2,432,874; 1,225,161.             
        + 2003-2004: 4,099,399; 2,453,984; 1,221,013.


# Part II - Age Groups 
The goal of this section is to explore the evolution of the population of the United States using different age groups. Population estimates by five-year age groups from 2010 to 2019 can be obtained from the U.S. Census Bureau web site (each year has its own table). To save time and make sure we all work with the same data, I downloaded the table for each year and compiled the information in a single Excel file. Download the Excel spreadsheet containing the Census bureau data on your computer. Each tab corresponds to a single year.     

1. Use the data in the spreadsheet to plot the age distribution of the U.S. population for different years.         
    a. Has there been major changes in the last 4 years of this data set?         
    b. The data set has 18 age groups. Use the age distributions that you just plotted to define larger age groups that can be used in a simplified model.     
    
2. Using recent [birth](./age_groups/nvsr67_01.pdf) and [death](./age_groups/nvsr65_04.pdf) rates estimates published by the Center for Disease Control and Prevention, create a model to predict the population in the age groups you defined, taking the 2010 data as initial condition. You may look at Figures 2 and 3 of the birth and deaths documents, respectively. (Note: do not attempt to print these files; they are more than 50 pages long!) Then, answer the following questions.         
    a. How does your model compare to the Census Bureau estimates for 2019?         
    b. Use your model to predict the population in each age group in 2050. What do you conclude?     
    c. To be more specific, you need to proceed as follows.         
        - Define the age groups you want to work with (do not pick too many groups; 3 or 5 should suffice).         
        - Estimate the birth and death rates for each age group. This will require estimating the birth and death rates of each age year within each age group, and calculating population-weighted birth and death rates for each age group.         
        - Use the Excel file to calculate the number of individuals in each of your age groups in 2010. This is the initial condition of your model.         
        - Assuming the birth and death rates you calculated for each age group are constant between 2010 and 2019, evolve your model to estimate the size of each age group for every year between 2011 and 2019.         
        - Compare the number of individuals in each age group predicted by your model for 2019 to the 2019 Census bureau data provided in the Excel spreadsheet. Comment on any difference.
