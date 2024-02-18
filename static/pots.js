let pots = {
    savings: { balance: 0, goal: 0 },
    holidays: { balance: 0, goal: 0 },
    groceries: { balance: 0, goal: 0 }
};


function deposit(pot) {
    let amount = parseInt(prompt("Enter amount to deposit:"));
    if (!isNaN(amount) && amount > 0) {
        pots[pot].balance += amount;
        updateBalance(pot);
    }
}


function withdraw(pot) {
    let amount = parseInt(prompt("Enter amount to withdraw:"));
    if (!isNaN(amount) && amount > 0 && amount <= pots[pot].balance) {
        pots[pot].balance -= amount;
        updateBalance(pot);
    } else {
        alert("Invalid amount or insufficient balance!");
    }
}


function updateBalance(pot) {
    document.getElementById(pot + "Balance").innerText = pots[pot].balance;
}


function addNewPot() {
    document.getElementById("popup").style.display = "block";
}


function remove(pot) {
    if (confirm("Are you sure you want to delete this pot?")) {
        document.getElementById(pot + "Pot").remove();
        delete pots[pot];
    }
}


function createPot() {
    let potName = document.getElementById("potName").value.trim();
    let amountGoal = parseInt(document.getElementById("amountGoal").value);
    if (potName && amountGoal > 0 && !document.getElementById(potName.toLowerCase() + "Pot")) {
        pots[potName.toLowerCase()] = { balance: 0, goal: amountGoal };
        let newPotHTML = `
        <div class="pot" id="${potName.toLowerCase()}Pot">
            <h2>${potName} Pot</h2>
            <p>Current balance: <span id="${potName.toLowerCase()}Balance">0</span></p>
            <p>Goal amount: <span id="${potName.toLowerCase()}Goal">${amountGoal}</span></p>
            <button onclick="deposit('${potName.toLowerCase()}')">Deposit</button>
            <button onclick="withdraw('${potName.toLowerCase()}')">Withdraw</button>
            <button onclick="remove('${potName.toLowerCase()}')">Remove</button>
        </div>`;
        document.getElementById("initialPots").insertAdjacentHTML('beforeend', newPotHTML);
        document.getElementById("popup").style.display = "none";
    } else if (document.getElementById(potName.toLowerCase() + "Pot")) {
        alert("Pot name already exists!");
    } else {
        alert("Please enter valid pot name and goal");
    }
}
