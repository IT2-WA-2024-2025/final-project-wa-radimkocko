function getRandomScore() {
    return Math.floor(Math.random() * 6);
  }
  
  function updateScores() {
    for (let i = 1; i <= 10; i++) {
      let match = document.getElementById(`football-score-${i}`).innerText.split(" - ");
      let home = match[0].trim();
      let away = match[1].trim();
  
      let homeScore = getRandomScore();
      let awayScore = getRandomScore();
  
      document.getElementById(`football-score-${i}`).innerText = `${home} ${homeScore} - ${awayScore} ${away}`;
    }
  
    for (let i = 1; i <= 10; i++) {
      let match = document.getElementById(`hockey-score-${i}`).innerText.split(" - ");
      let home = match[0].trim();
      let away = match[1].trim();
  
      let homeScore = getRandomScore();
      let awayScore = getRandomScore();
  
      document.getElementById(`hockey-score-${i}`).innerText = `${home} ${homeScore} - ${awayScore} ${away}`;
    }
  
    for (let i = 1; i <= 10; i++) {
      let match = document.getElementById(`tennis-score-${i}`).innerText.split(" def. ");
      let player1 = match[0].trim();
      let player2 = match[1].split(" ")[0].trim();
  
      let score1 = getRandomScore();
      let score2 = getRandomScore();
  
      document.getElementById(`tennis-score-${i}`).innerText = `${player1} def. ${player2} ${score1}-${score2}`;
    }
  }
  
  setInterval(updateScores, 30000);
  