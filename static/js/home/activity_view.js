// Creating an array from the elements that has SAIB class.
let sAIB = document.querySelectorAll(".SAIB"),
// Creating an array from the elements that has SATB class.
    sATB = document.querySelectorAll(".SATB");

function classifyElements() {
    // A function which sets the class attribute of specific elements. 

    // Looping through each element in sAIB array
    for (let i = 0; i < sAIB.length; i++) {
        // Creating a boolean variable called oddOrEvenIdent which returns true if the division of an integer is giving another integer
        let oddOrEvenIdent = Number.isInteger(i / 2)
    
        // If a number's divison to 2, gives an integer, that means that number is an even number.
        // Checking if the oddOrEvenIdent variable is equal to false which it's equal to an odd number
        if ( oddOrEvenIdent == false ) {
            // Setting the element's class to SAIB RightSAIB
            sAIB[i].setAttribute("class", "SAIB RightSAIB");
            // Setting the element's cass to SATB RightSATB
            sATB[i].setAttribute("class", "SATB RightSATB");
        
        // Checking if the oddOrEvenIdent variable is equal to true which it's equal to an odd number
        } else {
            // Setting the element's class to SAIB LeftSAIB
            sAIB[i].setAttribute("class", "SAIB LeftSAIB");
            // Setting the element's class to SAIB LeftSATB
            sATB[i].setAttribute("class", "SATB LeftSATB");
        }
    }
}

// Calling the classifyElements function.
classifyElements()