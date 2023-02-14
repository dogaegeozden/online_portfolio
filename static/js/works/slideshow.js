// Creating a variable called prevBtn by selecting the element which has PrevBtn class. 
let prevBtn = document.querySelector(".PrevBtn"),
// Creating a variable called nextBtn by selecting the element which has NextBtn class.
    nextBtn = document.querySelector(".NextBtn"),
// Creating an array called graphicDesignSlides by selecting all the elements which has GDS class.
    graphicDesignSlides = document.querySelectorAll(".GDS"),
// Creating a variable called numberOfSlides from the length of the graphicDesingSlides variable.
    numberOfSlides = graphicDesignSlides.length,
// Creating a variable called slideIndex and initializing with 0.
    slideIndex = 0;

function hideTheElements(){
    // A function which changes the display attribute of graphic design elements to none except the first one.

    // Looping through graphicDesignSlides' length
    for (let i = 0; i < graphicDesignSlides.length; i++) {
        // Changing the graphicDesignSlides element's display attribute to none.
        graphicDesignSlides[i].style.display = "none";
    }
    // Changing the display attribute of the first graphicDesignSlide element to block. Hint: This is the graphicDesignSlides element which will going to be displayed initially.
    graphicDesignSlides[slideIndex].style.display = "block";
}

function centerAlignVertically(){
    // A function which center aligns the first slide vertically.

    // Creating a variable called theSlideShowCont by selecting all the elements which has GDSCont and targeting a specific one using a index value.  
    let firstSlideShowCont = document.querySelectorAll(".GDSCont")[0],
    // Creating a variable called theSlideShowContsHeight and initializing it with theSlideShowCont element's height. 
        firstSlideShowContHeight = firstSlideShowCont.offsetHeight,
    // Creating a variable called reqM. Hint: This variable is equal to the amount of pixels that theSlideShowCont element needs to be center aligned.
    reqM = (graphicDesignSlides[0].offsetHeight / 2) - (firstSlideShowContHeight / 2);
    // Pusing the element from top to center align it vertically.
    firstSlideShowCont.style.top = `${reqM}px`;
}

function addFunctionsToSlideShowButtons(){
    // A function which adds functions to slide show buttons.

    // Checking if the prevBtn is exists.
    if (prevBtn){
        // Connecting the prevBtn with the showPrevSlide function as the function will going to trigger with a click.
        prevBtn.addEventListener("click", showPrevSlide);
    }
    // Checking if the nextBtn is exists.
    if (nextBtn){
        // Connecting the nextBtn with the showNextSlide function as the function will going to trigger with a click.
        nextBtn.addEventListener("click", showNextSlide);
    }
}

function showPrevSlide(){
    // A function which shows tne previous slide. 

    // Changing the display attribute of the first slide show element to none.
    graphicDesignSlides[slideIndex].style.display = "none";
    // Decreasing the slideIndex variable's value.
    slideIndex = slideIndex - 1;
    // Checking if the slideIndex variable's value is smaller than 0.
    if ( slideIndex < 0) {
        // Decreasing the slideIndex variable's value.
        slideIndex = numberOfSlides-1;
    }
    // Changing the first graphicDesignSlides element's display attribute to none. Hint: Displaying the first graphic design slide.
    graphicDesignSlides[slideIndex].style.display = "block";
    // Creating a variable called theSlideShowCont by selecting all the elements which has GDSCont and targeting a specific one using a index value.  
    let theSlideShowCont = document.querySelectorAll(".GDSCont")[slideIndex],
    // Creating a variable called theSlideShowContsHeight and initializing it with theSlideShowCont element's height. 
        theSlideShowContsHeight = theSlideShowCont.offsetHeight,
    // Creating a variable called reqM. Hint: This variable is equal to the amount of pixels that theSlideShowCont element needs to be center aligned.
        reqM = (graphicDesignSlides[slideIndex].offsetHeight / 2) - (theSlideShowContsHeight / 2);
    // Pusing the element from top to center align it vertically.
    theSlideShowCont.style.top = `${reqM}px`;
}

function showNextSlide(){
    // A function which shows the next slide.

    // Changing the display attribute of the firstt slide show element to none.
    graphicDesignSlides[slideIndex].style.display = "none";

    // Increasing the slide index by one 
    slideIndex = slideIndex + 1;
    // Checking if the slideIndex's value is greater than numberOfSlides value - 1.
    if ( slideIndex > numberOfSlides-1 ) {
        // Setting the slideIndex to 0
        slideIndex = 0;
    }
    // Setting the element's display css attribute to block.
    graphicDesignSlides[slideIndex].style.display = "block";
    // Creating an array called theSlidesShowCont by selecting all the elements which has GDSCont class.
    let theSlideShowCont = document.querySelectorAll(".GDSCont")[slideIndex],
        // Creating a variable called theSlideShowContsHeight from the theSlideShowCont element's height
        theSlideShowContsHeight = theSlideShowCont.offsetHeight,
        // Creating a variable called reqM by calculating the amount of distance that the element needs to be center align vertically.
        reqM = (graphicDesignSlides[slideIndex].offsetHeight / 2) - (theSlideShowContsHeight / 2);
    // Pushing theSlideShowCont variable from top.
    theSlideShowCont.style.top = `${reqM}px`;
}

// Calling the hideTheElements function.
hideTheElements()
// Calling the centerAlignVertically function.
centerAlignVertically()
// Calling the addFunctionsToSlideShowButtons function.
addFunctionsToSlideShowButtons()