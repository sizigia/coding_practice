function subReddit(link) {
    return link.match(/(\w+)/g)[5];
}

console.log(subReddit("https://www.reddit.com/r/relationships/"), "relationships")
console.log(subReddit("https://www.reddit.com/r/mildlyinteresting/"), "mildlyinteresting")
console.log(subReddit("https://www.reddit.com/r/funny/"), "funny")
console.log(subReddit("https://www.reddit.com/r/CrappyDesign/"), "CrappyDesign")
console.log(subReddit("https://www.reddit.com/r/confession/"), "confession")
console.log(subReddit("https://www.reddit.com/r/AskMen/"), "AskMen")
console.log(subReddit("https://www.reddit.com/r/comics/"), "comics")
console.log(subReddit("https://www.reddit.com/r/lifehacks/"), "lifehacks")
console.log(subReddit("https://www.reddit.com/r/wholesomememes/"), "wholesomememes")
console.log(subReddit("https://www.reddit.com/r/iamverysmart/"), "iamverysmart")
console.log(subReddit("https://www.reddit.com/r/starterpacks/"), "starterpacks")
console.log(subReddit("https://www.reddit.com/r/awww/"), "awww")