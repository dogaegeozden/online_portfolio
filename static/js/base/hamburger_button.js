// Creating a variable called hamburgerBtn by selecting the element which has Icon class from the DOM. 
let hamburgerBtn = document.querySelector(".Icon"),
// Creating a variable called dropDownBtn by selecting the element which has DropBtn from the DOM.
    dropDownBtn = document.querySelector(".DropBtn");

function dropDownBtnFunc() {
    // A function which opens the drop down menu.

    // Creating an element called dropDownCont by selecting the element which has DropDownContent class.
    let dropDownCont = document.querySelector(".DropDownContent");
    // Creating a variable called dDCA by getting the dropDownCont element's class attribute's value 
    let dDCA = dropDownCont.getAttribute("class");

    // Checking if dDCA is equal to "DropDownContent"
    if ( dDCA == "DropDownContent" ) {
        // Changing the dropDownCont element's display attribute
        dropDownCont.style.display = "block";
        // Setting the dropDownCont element's class to "DropDownContent Close" 
        dropDownCont.setAttribute("class", "DropDownContent Close");
        // Creating a variable called dropDownBtnIco by selecting the element which has "fa-caret-up" class from the DOM.
        let dropDownBtnIco = document.querySelector(".fa-caret-up");
        // Setting the dropDownBtnIco element's class to "fa-solid fa-caret-down"
        dropDownBtnIco.setAttribute("class", "fa-solid fa-caret-down");
    // Checking if dDCA's class is equal to "DropDownContent"
    } else if ( dDCA == "DropDownContent Close" ) {
        // Changing the dropDownCont element display attribute's value to none.
        dropDownCont.style.display = "none";
        // Setting the dropDownCont element's class attribute's value to "DropDownContent"
        dropDownCont.setAttribute("class", "DropDownContent");
        // Creating a variable called dropDownBtnIco by selecting the element which has "fa-caret-down" class from the DOM. 
        let dropDownBtnIco = document.querySelector(".fa-caret-down");
        // Setting the dropDownBtnIco element's class to "fa-solid fa-caret-up"
        dropDownBtnIco.setAttribute("class", "fa-solid fa-caret-up");
    }
}

function hamburgerBtnFunc() {
    // A function which changes 

    // Creating a variable called navBar by selecting element which has MyTopNav class from the DOM.
    var navBar = document.getElementById("MyTopNav");
    // Creating an element called dropDownCont by selecting the element which has DropDownContent class.
    let dropDownCont = document.querySelector(".DropDownContent");
    // Creating a variable called dDCA by getting the dropDownCont element's class attribute's value 
    let dDCA = dropDownCont.getAttribute("class");
    // Calling the dropDownBtnFunc
    if ( dDCA == "DropDownContent Close" ) {
        // Changing the dropDownCont element display attribute's value to none.
        dropDownCont.style.display = "none";
        // Setting the dropDownCont element's class attribute's value to "DropDownContent"
        dropDownCont.setAttribute("class", "DropDownContent");
        // Creating a variable called dropDownBtnIco by selecting the element which has "fa-caret-down" class from the DOM. 
        let dropDownBtnIco = document.querySelector(".fa-caret-down");
        // Setting the dropDownBtnIco element's class to "fa-solid fa-caret-up"
        dropDownBtnIco.setAttribute("class", "fa-solid fa-caret-up");
    }
    // Creating a lambda function which checks if the navBar element's class name is equal to TopNav and if the statment is true adds an another class name called responsive to make the navigation bar responsive.
    "TopNav" === navBar.className ? navBar.className += " Responsive" : navBar.className = "TopNav"
}

// Connecting the hamburgerBtn with the hamburgerBtnFunc as the function will going to trigger with a button click.
hamburgerBtn.addEventListener("click", hamburgerBtnFunc);
// Connecting the dropDownBtn with the dropDownBtnFunc function as teh function will going to trigger with a click.
dropDownBtn.addEventListener("click", dropDownBtnFunc);