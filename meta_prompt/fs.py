fs_prompt = """Example 1:
Original Post (OP)'s title: CMV: Anything that is man-made is natural.
Original Post (OP)'s text: I can't remember the topic that spurred this discussion, but a friend and I were debating whether man-made things were natural. He took the position that they are unnatural. He cited this definition by Merriam-Webster: existing in nature and not made or caused by people : coming from nature as his basis for the distinction for natural vs. unnatural. However, I respectfully disagree with his position and furthermore that definition of natural. People arise from nature. Humankind's capacity to create, problem-solve, analyze, rationalize, and build also come from natural processes. How are the things we create unnatural? It is only through natural occurrences that we have this ability, why is it that we would give the credit of these things solely to man, as opposed to nature? We are not separate from nature, thus, how can any of our actions or creations be unnatural? If we were somehow separate from nature, I would understand the distinction between natural and man-made. However, I think unnatural and man-made are not synonyms by any means. It seems to me that man-made things MUST be natural due to our being part of nature.
Argument: Look at the definition you provided, if we remove the exclusion of things which humans create: "existing in nature and not made or caused by people." So essentially, by this definition, "natural things" are "things that exist," which is frankly rather meaningless. If one wanted to discuss the results of human activity we would then have to make up a new word which could be redefined by the same argument. The whole point of the word is to exclude human activity. If you remove that aspect, it simply ceases to have meaning.
Label: Positive

Example 2:
Original Post (OP)'s title: CMV: Anything that is man-made is natural.
Original Post (OP)'s text: I can't remember the topic that spurred this discussion, but a friend and I were debating whether man-made things were natural. He took the position that they are unnatural. He cited this definition by Merriam-Webster: existing in nature and not made or caused by people : coming from nature as his basis for the distinction for natural vs. unnatural. However, I respectfully disagree with his position and furthermore that definition of natural. People arise from nature. Humankind's capacity to create, problem-solve, analyze, rationalize, and build also come from natural processes. How are the things we create unnatural? It is only through natural occurrences that we have this ability, why is it that we would give the credit of these things solely to man, as opposed to nature? We are not separate from nature, thus, how can any of our actions or creations be unnatural? If we were somehow separate from nature, I would understand the distinction between natural and man-made. However, I think unnatural and man-made are not synonyms by any means. It seems to me that man-made things MUST be natural due to our being part of nature.
Argument: You're using natural to mean definition 8 "the universe, with all its phenomena." The more common definition is definition 1 "the material world, especially as surrounding humankind and existing independently of human activities." So by definition we are not part of nature, as nature is more commonly used, and is in this sense used, to refer to things that exist independently of human activities.
Label: Negative

Example 3:
Original Post (OP)'s title: CMV: Essential Oils are bullshit.
Original Post (OP)'s text: My wife has recently gotten deeply involved/obsessed with the healing properties of essential oils. I am cursed with a common problem in that I am an extremely skeptical person. I can't help but look at this product and see a pyramid scheme that takes advantage of the gullible. All the shit my wife watches on these oils is carefully worded to make sure they don't make actual healing claims, I'm told this is because they aren't FDA approved and could get in trouble. I've looked a little and haven't found anything debunking these oils but i still cannot help but feel they are total BS. I would love to get more information from unbiased sources on this.
Argument: [This answer in /r/askscience does a pretty good job of describing essential oils.](http://www.reddit.com/r/askscience/comments/2pp57r/how_effective_are_essential_oils/cmytzdq) As the comment points out there are benefits to essential oils if they are used in the right way. However, the current fad mixes the raw essential oils with other stuff that may or may not be good for you. The raw essential oils are actually "a vital resource for drug discovery."
Label: Positive

Prediction: predict whether the argument has successfully changed the OP's view. Respond with 'positive' if it has and 'negative' if it has not.

Original Post (OP)'s title: {title}
Original Post (OP)'s text: {text}
Argument: {argument}

Based on the above information, please give me your answer following these guidelines:
1. Your prediction should be explicitly stated as 'positive' or 'negative'.

The response is:""".strip()
