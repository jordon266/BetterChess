import logo from './logo.svg';
import './App.css';
import { useEffect, useState } from 'react'


function App() {
  // got from chess.com
  const [games, setGame] = useState([]);


  async function test(response) {
    const reader = response.body.getReader();
    const decoder = new TextDecoder("utf-8");
    const lineMatcher = /\n/;
    let num = 0;
    try {
      while (true) {
        const { done, value } = await reader.read();
        if (done) break;
        const chunk = decoder.decode(value, { stream: true });
        // chunkCount++;
        let parts = chunk.split(lineMatcher)
        if (chunk.includes('}{')) {
          let chunk_1 = chunk.replaceAll(/}{/g, "},,{")
          parts = chunk_1.split(/,,/)
          console.log('number of parts:' + parts.length)
        }
        for (let part of parts) {
        
            let game =JSON.parse(part)
            setGame(oldArray=>[...oldArray,game])
        }

      }

    } catch (error) {
      console.error('Stream processing error:', error);
    }
  
    return games;
  }



  useEffect(() => {
    const apiUrl = '/mygames';
    fetch(apiUrl) // being called twice --> solved
      .then(response => test(response)).then(games => console.log(games)) // console.log not working gotta see out fetch and then work
      .catch(error => console.error('error'));
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js {games.length}</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>

        <ol>
        {games.map(game=> {
          return <li>{game['id']}</li>;
        })}
        
        </ol>
      </header>
    </div>
  );
}

export default App;
