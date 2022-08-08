# DSEC FPL Data Challenge 2022/2023

Join DSEC FPL Leqgue, build data pipeline, analyze, visualize and story-tell the data

## Join-by date

You can join any time. It won't affect your chances for data engineering chalanges. 

Auto-join by visiting [this link](https://fantasy.premierleague.com/leagues/auto-join/szunr4).

The rules of FPL game are [here](https://fantasy.premierleague.com/help/rules)

## Winners

At the end of the season we establish a winner in every of the following categories:

- League winner (best result)
- Best data pipeline
- Best analytics
- Best dashboard / visualization
- Best data-bsed decision-making story-telling

Winning the league is self-explenatory. Winning the 4 other categories
will be established by voting. Every league member has one secret vote in every category.

If many people have the same winning result in any of the categories, 
they will be tossing the coin until the winners are established.

## Awards:

- Eternal fame
- Free pizza sponsored by your league coleagues

Winning all five categories won't make your stomach 5 times bigger. Hopefully.
Therefore one pizza will be allocated to the winner, no matter how many categories she or he wins.

## Rules of the chalenge

* Thou shell join the DSEC FPL league. 
* Thau shell use data in making decisions
* Thau shell aspire to beat the "crazy chicken" player, who makes choices with random "set & foget" strategy
* Thau will share his organized source data with the group
* Thau may story-tell their decision-making to the group
* Thau may share his data pipeline design with the group
* Thau may share his analysis methods with the group
* Thau may share his dashboard or visualisation with the group

## Starting point

1. You can choose players from "elements" in below api url:
https://fantasy.premierleague.com/api/bootstrap-static/

2. The api has other data elements, can be useful

3. Below random selector can be helpful to start coding

```sh
# works with python 3.9.13, but not with 3.10.5 (requests lib)
cd selector_random
python -m venv .venv
source .venv/bin/activate
python -m pip install requests pytest
pytest
python main.py
```

## Coding

If you code: 

- Code in whatever language you like
- Divide your code how you like 
	- you feel one repo for your purpose is right? Go for it!
	- you think few repos make more sense? Not a bother.
	
You'll be making this kinds of decisions all the time. It's great if you
can share your thinking with the group afterwards.

## Data pipeline sharing

If you build a data pipeline, make it so that other mambers could run it
and receive the output data.

## Data Sharing

- share the data whatever way you think is right
- organize the data whatever way you think is right

## Dashboard sharing

- share the dashboard however you like
- walk us through your dasbhoard at the DSEC meeting

## Best data story-telling

- schedule a talk on DSEC
- walk us through your thinking and how you used data to make your cecisions

## Useful resources
1. [Josh Bull's video](https://www.youtube.com/watch?v=LzEuweGrHvc&t=1268s)
Josh is Oxford's PhD who dedicates to mathemathical biology. He applies mathemathical modeling to camcer studies. He won the world's FPL in 2019. In the video he shows some of the 
methods he used and some of his findings.

2. [vaastav/Fantasy-Premier-League](https://github.com/vaastav/Fantasy-Premier-League) github repository

Great repository, historical data, lots of linked analysis

3. fpl package

```sh
pip install fpl
```
