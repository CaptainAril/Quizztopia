// const startButton = document.getElementById('start-btn')
// const questionContainerElement = document.getElementById('question-container')

$(document).ready(function() {

    // Check for click events on the navbar burger icon
    $(".navbar-burger").click(function() {
  
        // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
        $(".navbar-burger").toggleClass("is-active");
        $(".navbar-menu").toggleClass("is-active");
  
    });
  });

  
submitButton.addEventListener('click', startGame)

function startGame(){
    console.log('started')
    startButton.classList.add('hide')
    questionContainerElement.classList.remove('hide')
    setNextQuestion()
}

function setNextQuestion(){

}

function selectAnswer(){

}

const questions = [
    {
        question: 'what is 2 + 2',
        answer: [
            {text: '4', correct: true},
            {text: '22', correct: false}
        ]
    }
]

