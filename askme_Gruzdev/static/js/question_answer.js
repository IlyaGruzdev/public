function questionAnswersDisp(question_id)
{
  var id="question " + question_id;
  var element=document.getElementById(id);
  var answers=element.getElementsByClassName('card')
  for(i=0; i<answers.length; i++)
  {
    if(answers[i].style.display=="none")
    answers[i].style.display="";
    else
    answers[i].style.display="none";
  } 
  
}