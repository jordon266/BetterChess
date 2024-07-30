import logo from './logo.svg';
import './App.css';
import { useEffect, useState } from 'react'
import { getGames } from './utils';

function App() {
  // got from chess.com
  const [wgames, setWhiteGame] = useState([]);
  const [bgames, setBlackGame] = useState([]);

  // async function test(response) {
  //   const reader = response.body.getReader();
  //   const decoder = new TextDecoder("utf-8");
  //   const lineMatcher = /\n/;
  //   let num = 0;
  //   try {
  //     while (true) {
  //       const { done, value } = await reader.read();
  //       if (done) break;
  //       const chunk = decoder.decode(value, { stream: true });
  //       // chunkCount++;
  //       let parts = chunk.split(lineMatcher)
  //       if (chunk.includes('}{')) {
  //         let chunk_1 = chunk.replaceAll(/}{/g, "},,{")
  //         parts = chunk_1.split(/,,/)
  //         console.log('number of parts:' + parts.length)
  //       }
  //       for (let part of parts) {

  //           let game =JSON.parse(part)
  //           setGame(oldArray=>[...oldArray,game])
  //       }

  //     }

  //   } catch (error) {
  //     console.error('Stream processing error:', error);
  //   }

  //   return games;
  // }



  useEffect(() => {
    const whitegames = '/mygames/white';
    const blackgames = '/mygames/black';
    fetch(whitegames) // being called twice --> solved
      .then(response => getGames(response, setWhiteGame, wgames)).catch(error => console.error('error'));
    fetch(blackgames) // being called twice --> solved
      .then(response => getGames(response, setBlackGame, bgames, 'black')).catch(error => console.error('error'));
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js {wgames.length}</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          
        </a>
        White Games
        <ol>
          {wgames.map(game => {
            return <li>{game['id'] + '  ' + game['speed']  + '  ' +  game['winner']}</li>;
          })}

        </ol>
        Black Games
        <ol>
          {bgames.map(game => {
             return <li>{game['id'] + '  ' + game['speed']  + '  ' +  game['winner']}</li>;
          })}

        </ol>
      </header>
    </div>
  );
}

export default App;
