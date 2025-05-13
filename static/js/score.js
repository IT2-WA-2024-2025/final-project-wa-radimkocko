const finishedMatches = new Set();
const matchScoreCaps = {};

function getScoreIncrement() {
  return Math.floor(Math.random() * 3);
}

function getOrCreateScoreCap(id) {
  if (!matchScoreCaps[id]) {
    matchScoreCaps[id] = Math.floor(Math.random() * 5) + 6;
  }
  return matchScoreCaps[id];
}

function updateScores() {
  for (let i = 1; i <= 10; i++) {
    const types = ['football', 'hockey', 'tennis'];
    
    for (const type of types) {
      const matchId = `${type}-score-${i}`;
      if (finishedMatches.has(matchId)) continue;

      const el = document.getElementById(matchId);
      if (!el) continue;

      if (type === 'tennis') {
        const match = el.innerText.match(/^(.*?)\s+def\.\s+(.*?)\s+(\d+)-(\d+).*$/);
        if (match) {
          const player1 = match[1].trim();
          const player2 = match[2].trim();
          let score1 = parseInt(match[3]);
          let score2 = parseInt(match[4]);

          const cap = getOrCreateScoreCap(matchId);

          score1 += getScoreIncrement();
          score2 += getScoreIncrement();

          if (score1 >= cap || score2 >= cap) {
            el.innerText = `${player1} def. ${player2} ${score1}-${score2} (Konec)`;
            finishedMatches.add(matchId);
          } else {
            el.innerText = `${player1} def. ${player2} ${score1}-${score2}`;
          }
        }
      } else {
        const match = el.innerText.match(/^(.*?)(\d+)\s*-\s*(\d+)(.*?)$/);
        if (match) {
          const team1 = match[1].trim();
          const team2 = match[4].trim();
          let score1 = parseInt(match[2]);
          let score2 = parseInt(match[3]);

          const cap = getOrCreateScoreCap(matchId);

          score1 += getScoreIncrement();
          score2 += getScoreIncrement();

          if (score1 >= cap || score2 >= cap) {
            el.innerText = `${team1} ${score1} - ${score2} ${team2} (Konec)`;
            finishedMatches.add(matchId);
          } else {
            el.innerText = `${team1} ${score1} - ${score2} ${team2}`;
          }
        }
      }
    }
  }
}

document.addEventListener("DOMContentLoaded", function () {
  updateScores();
  setInterval(updateScores, 15000);
});
