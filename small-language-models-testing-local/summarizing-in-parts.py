import requests

API_URL = "https://api-inference.huggingface.co/models/sshleifer/distilbart-cnn-12-6"
headers = {"Authorization": "Bearer *token_here*"}

MAX_SEGMENT_LENGTH=1000

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

text_for_summary="""
Washington

CNN
 — 
Former President Donald Trump is on a lying spree.

As Election Day draws nearer, the Republican presidential nominee has made false claim after false claim on a dizzying variety of subjects. He has both come up with new falsehoods on pressing issues, most notably the federal response to Hurricane Helene and Hurricane Milton, and repeated old favorites about subjects he has been railing about since his 2016 presidential campaign.

We went through the speeches Trump made at his two Wednesday campaign rallies in the critical swing state of Pennsylvania, one in Scranton and one in Reading. In those two addresses alone, he uttered at least 40 separate false claims.

Here is a fact check.

FEMA and migrants: Trump falsely claimed of the Federal Emergency Management Agency: “They have no money. You know where they gave the money? To illegal immigrants coming in.” He also said, “They spent all their funds; they have no funds to take care…”

This is false in two ways. FEMA does have money for the immediate responses to Hurricane Helene and Hurricane Milton, though a string of recent disasters has depleted its disaster relief fund; the fund had about $11 billion remaining as of Wednesday. And FEMA did not give all of its disaster relief money to undocumented people; rather, as mandated by Congress, FEMA also administers an entirely separate pool of money for sheltering migrants.

FEMA and employees: Trump added another false claim about FEMA, saying: “They have no workers, they have no nothing.” FEMA has more than 20,000 employees.

Harris and the response: Trump falsely claimed that as desperate people tried to survive Hurricane Helene in North Carolina, Vice President Kamala Harris “didn’t send anything or anyone at all” to help them. There were extensive federal and state rescue and relief efforts in the immediate aftermath of Hurricane Helene. It’s true that some residents died and others were stranded for days, but the state was not ignored by Harris or the Biden administration; North Carolina Gov. Roy Cooper, a Democrat, has repeatedly thanked President Joe Biden for his assistance.

Schools and transgender children: Trump told a slightly vaguer version of his usual false story about schools supposedly obtaining or performing gender-affirming surgeries for transgender children behind their parents’ backs, saying, “Your child go goes to school, and they take your child. It was a ‘he.’ And comes back a ‘she.’ And they do this…And often without parental consent.”

There is no evidence that US schools have sent children into gender-affirming surgeries without their parents knowing or performed gender-affirming surgeries on site; Trump’s own presidential campaign could not provide a single example of any of this ever happening. Even in states where gender-affirming surgery is legal for people under age 18, parental consent is required before a minor can undergo such a procedure.

Trump’s opponents and the election: In Reading, Trump falsely claimed of his election opponents: “They are cheatin’ dogs, I will tell you that.” In Scranton, he falsely claimed, “Their first meeting is: ‘How do we cheat?’” This is all nonsense. There is no basis for the claim that Trump’s opponents are election cheaters.

Harris’ previous presidential campaign: Trump repeated his false claim that, when Harris ran for president in 2020, “she was the first one to drop out, of like 22 people” in the Democratic primary. In fact, 13 other Democratic candidates dropped out of that primary before Harris exited in December 2019 – including the sitting or former governors of Washington, Montana and Colorado; the sitting mayor of New York City; and sitting or former members of the House of Representatives and Senate.

Harris and the press: Trump falsely claimed of Harris: “She doesn’t do any interviews.” Trump is entitled to argue that Harris has not done a sufficient number of interviews as the Democratic presidential nominee, but the assertion she doesn’t do “any” is wrong; Harris has done multiple interviews in recent weeks. Notably, Harris did an interview with the CBS News show “60 Minutes,” which aired Monday, while Trump backed out of his own interview with the show.

Harris-Walz and the Supreme Court: After correctly noting that Harris’ running mate, Minnesota Gov. Tim Walz, recently expressed support for getting rid of the Electoral College, Trump falsely claimed, “They want to add… they’re thinking about – first time I heard this number – 25: they want to have 25 Supreme Court justices.” There is no basis for the claim that Harris or Walz is pushing for a 25-justice Supreme Court.

Walz and menstrual products in schools: Trump disparaged Walz as “Tampon Tim,” then said, “You know why they call him that? ’Cause they sell tampons, with special legislation, in boys’ locker rooms.” Trump’s claim is false. The law Walz signed in 2023 requires schools to provide free menstrual products in bathrooms, not the sale of menstrual products in locker rooms – and all 18 public school districts that responded to CNN’s questions about the law say they do not provide the products in boys’ bathrooms. You can read more here.

Wind power: Trump repeated a familiar nonsensical story about how the use of wind power means people “can’t watch” television if “there’s no wind tonight.” Using wind power as part of a mix of power sources does not cause power outages when the wind isn’t blowing, as the federal Department of Energy explained on its website even during the Trump administration.

The Biden administration and electric vehicles: Trump falsely claimed that under a Biden administration electric vehicle mandate, “everybody’s got to have an electric car almost immediately.” There is no Biden administration requirement that consumers must buy an electric car or give up their existing gas-powered cars, “almost immediately” or otherwise. The Biden administration has made a push to get automakers to reduce emissions and adopt electric vehicles, but there is not a mandate for consumers; the tailpipe rules for automakers that were unveiled by the administration earlier this year aim to have electric vehicles make up 35% to 56% new vehicles sold in 2032.

The Paris climate accord and emissions: Trump repeated his false claim that under the Paris climate accord, the US “had to pay a trillion dollars” while some other countries didn’t have to pay.

Trump’s “trillion” figure is a wild exaggeration. Under the Obama administration, the US paid $1 billion of a $3 billion commitment it originally made in 2014. After Trump pulled the country out of the Paris accord, the US paid nothing to the global finance goal. And while Biden pledged $11.4 billion annually from the US, this level of funding hasn’t materialized. That’s because Congress, responsible for appropriating the nation’s budget, has allocated only a fraction of that – roughly $1 billion in 2022. 

Harris’ comments on fracking: Trump said, “Listen to Kamala in her own words very recently,” then played two video clips in which Harris said she was in favor of banning fracking. But those clips are from 2019, beyond any reasonable definition of “very recently.” Harris has said during the 2024 campaign that she no longer favors banning fracking.

Venezuela, prisons and migration: Trump falsely claimed, “In Venezuela, many countries, they’re emptying their prisons into our country.” This is false. Trump has never corroborated this claim about Venezuela, let alone “many countries,” and experts have told CNN, PolitiFact and FactCheck.org that they know of no evidence for it.

“We have no evidence that the Venezuelan government is emptying its prisons or mental health institutions to send them outside the country, in other words, to the U.S. or any other country,” Roberto Briceño-León, founder and director of the Venezuelan Observatory of Violence, an independent organization that tracks violence in the country, said in an email to CNN in June, after Trump made similar claims.  

Venezuela, criminals and migration: Adding another colorful story about Venezuela, Trump falsely claimed that “they take the criminal gangs from Caracas off the streets and they bus them into the United States and drop them.” This is false. There is no evidence of Venezuelan authorities somehow busing gang members into the US.

The world prison population: Trump repeated his false claim that “the prison population all over the world is down, because they put them in our country.” The recorded global prison population increased from October 2021 to April 2024, from at least about 10.77 million people to at least about 10.99 million people, according to the World Prison Population List compiled by experts in the United Kingdom.

“I do a daily news search to see what’s going on in prisons around the world and have seen absolutely no evidence that any country is emptying its prisons and sending them all to the US,” Helen Fair, co-author of the prison population list and research fellow at the Institute for Crime & Justice Policy Research at Birkbeck, University of London, said in June, when Trump made a similar claim.

The number of migrants: Trump, speaking about migration, falsely claimed that “21 million people – plus – came into our nation” under the Biden-Harris administration. Through August, the country had recorded about 10.3 million nationwide “encounters” with migrants during the Biden-Harris administration, including millions who were rapidly expelled from the country; even adding in so-called “gotaways” who evaded detection, estimated by House Republicans as being roughly 2 million, there’s no way the total is “21 million.”

Harris, migrants and criminals: Trump, criticizing Harris on immigration, again wrongly described a set of statistics that was released in September. He falsely claimed in Scranton, “You saw that last week: 13,099 murderers allowed to come in, through them.” He falsely claimed in Reading that “as we speak she has – and this was just announced last week – 13,099, so over 13,000 illegal alien convicted murderers, roaming free in our country.”

This 13,099 figure includes people who are incarcerated in federal, state and local prisons and jails – and it includes people who entered the country over decades, including during Trump’s administration, not just under Biden and Harris. You can read more here.

Harris’ record as attorney general: Trump falsely claimed that when Harris was attorney general of California, “she said under no circumstances” will people be prosecuted for the crimes of child sex trafficking, assault with a deadly weapon or the rape of an unconscious person. Harris did not say anything like that; Trump was grossly mischaracterizing a debate over the language Harris’ office used to summarize California ballot initiatives.

Trump’s border wall: Trump repeated his false claim that “I built over 500 miles of wall” on the southern border. Official government data shows 458 miles were built under Trump – including both wall built where no barriers had existed before and wall built to replace previous barriers.

Trump’s crowds: Trump falsely claimed of his rallies: “We never have an empty seat.” There have been empty seats at numerous Trump rallies over the years – including hundreds at this very rally in Reading. And at many Trump rallies, some once-filled seats empty out during his speeches when supporters leave.

Trump’s crowd in Butler: Trump falsely claimed there were “over 100,000 people” at the rally he held Saturday in Butler, Pennsylvania, at the same site where a gunman had attempted to assassinate him in July. CNN affiliate KDKA in Pittsburgh reported that the Secret Service put the crowd at 24,000 people, while the Trump-supporting sheriff of Blair County, Pennsylvania, James Ott, said in his speech at the rally itself (more than three hours before Trump took the stage) that he was looking out at “21,000-plus people.”

Trump’s response to the assassination attempt: Trump, speaking of his response to the attempted assassination in July, falsely claimed, “I said as I was getting up – before I even got up – I said, ‘How many people were killed?’ Because, you know, it was wall to wall people, and I said, ‘How many people were killed?’ They said, ‘We think three, sir,’ and I said, ‘That’s not good.’”

Trump’s rally microphone picked up what was said by Trump and Secret Service agents while he was on the ground and just after, and he did not ask, before or after he got up, how many people were killed. It’s possible he did so after he was whisked off stage (and, of course, possible he was genuinely misremembering what happened in such a traumatic moment).

Trump and firefighters: Trump falsely claimed, “We got the firefighters endorse us, you probably heard.” But the actual recent national news was that the International Association of Firefighters had decided not to endorse any candidate in the race; while Trump is free to argue that this was a victory for him, given that the union endorsed Biden in 2020, it was not an actual endorsement. And while there were some people in the Scranton crowd holding “Scranton Firefighters for Trump” signs, the Scranton chapter of the union also has not issued an endorsement. The president of the chapter told the Scranton Times-Tribune that none of the people he saw holding the signs were active or retired local firefighters.

Trump and classified documents: Speaking of the criminal case against him over his post-presidency retention of classified documents, Trump repeated his false claim that “I had the Presidential Records Act; I was totally allowed to do it.” The Presidential Records Act says that, the moment a president leaves office, the National Archives and Records Administration gets custody and control of all presidential records from their administration. (Trump’s case was dismissed by a federal judge in July on other grounds, that the appointment of special counsel Jack Smith was unconstitutional; Smith has appealed.)

The New York Times and the Russia investigation: Trump, calling claims about his 2016 campaign’s connections to Russia a “scam,” repeated his false claim that The New York Times “admitted they were wrong” about the coverage that won its journalists a Pulitzer Prize along with journalists from The Washington Post.

“The claim is completely false,” Times spokesperson Charlie Stadtlander said in an email to CNN in 2023, when Trump made a similar claim; Stadtlander noted that “the award was upheld by the Pulitzer Prize Board after an independent review” and said the Times’ reporting “was also substantiated by the Mueller investigation and Republican-led Senate Intelligence Committee investigation into the matter.”

The New York Times and the 2016 election: Trump repeated a false claim he made during his presidency, saying of The New York Times’ coverage of the 2016 election: “Remember in 2016 they had to do an editorial apologizing to their readers because they said, ‘He’s going to lose’…and then I won?”

As the Times noted in 2017 in response to such Trump claims, it did not apologize for its 2016 election coverage. It did publish a post-election letter, from then-executive editor Dean Baquet and publisher Arthur Sulzberger Jr., that said the election had raised several questions, including this: “Did Donald Trump’s sheer unconventionality lead us and other news outlets to underestimate his support among American voters?” But the letter did not include an apology, to Trump or anyone else.

Trump and the defeat of ISIS: Trump repeated his false claim that “we defeated ISIS in four weeks; it was supposed to take four or five years.” The ISIS “caliphate” was declared fully liberated more than two years into Trump’s presidency.

Military equipment surrendered to the Taliban: Trump repeated his false claim that “we gave $85 billion worth” of US military equipment to the Taliban. Trump’s figure is a massive exaggeration; the Pentagon has estimated that the equipment abandoned to the Taliban by Afghan forces upon their 2021 collapse was worth about $7.1 billion – a chunk of the roughly $18.6 billion worth of equipment provided to Afghan forces between 2005 and 2021.

Biden and foreign income: Trump repeated his false claim that “Biden got a lot of money from China.” After years of investigation by House Republicans, there is still no evidence Biden has received any Chinese money.

Chris Wallace and a question about the Biden family: Trump told his familiar false story about how he had asked Biden at a 2020 presidential debate why the wife of a mayor of Moscow had paid Biden $3.5 million – in fact, the money was sent to a firm connected to the president’s son Hunter Biden, not to the president – but moderator Chris Wallace, then of Fox News and now of CNN, had interjected to say, “Well, please don’t ask him that question.” Wallace never did that. As the transcript shows, Wallace interjected during this debate exchange to try to get Trump to allow Biden to answer Trump’s question about the payment, not to stop Trump from asking.

Inflation: Trump repeated his false claim that inflation under Biden and Harris is “the worst inflation in the history of our country.” Trump could fairly say that the US inflation rate hit a 40-year high in June 2022, when it was 9.1%, but that was not close to the all-time record of 23.7%, set in 1920, and the rate has since plummeted; the most recent available inflation rate at the time Trump spoke here was 2.5% in August.

Mortgage rates: Trump falsely claimed that young people can’t buy a house because interest rates are higher than 10%: “It’s not 10%, it’s 11, 12, 13, 14, 15 percent.” This is false. The average rate on a standard 30-year fixed mortgage was 6.12% in the week ending October 3, according to mortgage financing provider Freddie Mac, and 6.32% in the week ending October 10.

Trump’s tax cut: Trump repeated his false claim that “I gave you, as you know, the largest tax cut in the history of our country.” Expert analyses have found that his 2017 tax cut law was not the largest in US history, either in percentage of gross domestic product or in inflation-adjusted dollars.

Tariffs on China: Trump repeated two of his regular false claims about tariffs on imported Chinese products. He falsely claimed that China “paid hundreds of billions of dollars” in these tariffs during his presidency, then falsely claimed that before his presidency, “nobody ever brought in 10 cents, not one other – not 10 cents, you check those records.”

We’ve checked, and the truth is that the US was generating billions per year in revenue from tariffs on China before Trump took office; in fact, the US has had tariffs on Chinese imports since the 1700s. Second, US importers pay these tariffs, not China, and study after study has found that Americans bore the overwhelming majority of the cost of Trump’s tariffs.

The 1890s and tariffs: Touting the supposed benefits of tariffs, Trump falsely claimed that in the 1890s, when the US had very high tariffs, “Our country was the richest it ever was.” The US is far richer today than in the 1890s; per capita gross domestic product is now many times higher than it was then.

The trade deficit with China: Trump repeated his frequent false claim that the US trade deficit with China has averaged “$500 billion” per year. The US has never had a $500 billion trade deficit with China even if you only count trade in goods and ignore the services trade in which the US traditionally runs a surplus with China; the all-time record, about $418 billion, was set under Trump in 2018.

Harris and taxes: Trump played a deceptively edited video showing “The View” co-host Meghan McCain saying to Harris in 2019, “Everything from a 70 to 80% tax rate,” and Harris responding, “I think that’s fantastic.”

This video cuts out key words from the exchange; Harris was not specifically endorsing high tax rates when she made the “fantastic” comment.

Here’s the transcript of the 2019 exchange:

McCain: “Alexandria Ocasio-Cortez is the new darling of the party. She officially has more Twitter followers than Nancy Pelosi. She was on ‘60 Minutes’ this weekend proudly calling herself a radical. And she’s promoting policies like saying that every single carbon emission in the country, every car, should be eliminated within the next 11 years, everything from a 70 to 80 percent tax rate. Do you agree that she could possibly – and this ideology, of the socialist left – could splinter your party?”

Harris: “No. You know, I think that she is challenging the status quo. I think that’s fantastic. I think that – you know, I used to teach, before, especially before – in the last few years – and the thing that I always loved about teaching was when you teach, it requires you to defend the premise. And it requires you to re-examine the premise. And question, is it still relevant? Is it – does it have impact? Does it have meaning? And I think that she is introducing bold ideas that should be discussed. And I think it’s good for the party, I frankly think it’s good for the country. Let’s look at the bold ideas. And I’m eager that we have those discussions. And when we are able to defend status quo, then do it, and if there are – you know, if there’s not merit to that, then let’s explore new ideas.”

Biden’s documents case: Trump falsely claimed in Reading that, in an investigation into Biden’s handling of classified documents, “Biden was essentially convicted” and in Scranton that “they ruled on him, they said he’s guilty.” Biden was not convicted, “essentially” or not, and was not found guilty; in fact, Biden was not even charged with a crime. The special counsel in the case, Robert Hur, wrote in his public report that “the evidence does not establish Mr. Biden’s guilt beyond a reasonable doubt,” adding that “several defenses are likely to create reasonable doubt as to such charges.”

A supposed Biden gaffe: Mocking Biden’s gaffes, Trump falsely claimed, “But the worst was when he was in New Hampshire and he said, ‘It’s great to be in Florida.’ That’s palm trees.” This never happened. Biden has certainly made various geographic gaffes, as has Trump, but he never said he was in Florida when he was actually in New Hampshire.
"""
print(len(text_for_summary))

def splitIntoSegments(text):
	new_array=[""]

	text_in_array=text.split("\n")
	print(len(text_in_array))
	text_in_array=list(filter(lambda a: a != "", text_in_array))
	section_length=0
	new_array_index=0
	for line in text_in_array:
		if(section_length+len(line)<MAX_SEGMENT_LENGTH):
			section_length=section_length+len(line)+1
			new_array[new_array_index]=new_array[new_array_index]+" "+line
		else:
			new_array.append("")
			new_array_index=new_array_index+1
			section_length=0
	
	return new_array

def summarizeParts(arr):
	new_text=""
	for elem in arr:
		# print(len(elem))
		out = query({
			"inputs": elem,
		})
		print(f"Summarized a part...")
		new_text+=out[0]["summary_text"]+"\n\n"
	
	return new_text

while (len(text_for_summary)>4000):
	arr_for_summary=splitIntoSegments(text_for_summary)
	text_for_summary=summarizeParts(arr_for_summary)

print(text_for_summary)



# print(len(new_array))
# for elem in new_array:
# 	print(elem+"\n\n\n\n")



# output = query({
# 	"inputs": text_for_summary,
# })

# print(output)