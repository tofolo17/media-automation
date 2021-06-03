const users = [];

for (let i = 0; i < document.getElementsByClassName("FPmhX").length; i++) {
    users.push(document.getElementsByClassName("FPmhX")[i].text)
}

console.log(users)
