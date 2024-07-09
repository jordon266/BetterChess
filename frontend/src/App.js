import logo from './logo.svg';
import './App.css';
import { useEffect, useState } from 'react'

function App() {
  // got from chess.com
  const [numOfGames, setnumOfGames] = useState(0);
  async function test(res) {
    const reader = res.body.getReader();
    console.log(res.body)
    const decoder = new TextDecoder();
    let num = 0
    reader.read().then(function processChunk({ done, value }) {
      if (done) return;
      const chunk = decoder.decode(value, { stream: true });
      num+=1
      console.log(`Received chunk: ${chunk}`);
      console.log(num)
      // Process the chunk here
      return reader.read().then(processChunk);
    });
  }

  useEffect(() => {
    const apiUrl = '/mygames';
    fetch(apiUrl)
.then(response => test(response))
  .catch(error => console.error(error));
})


  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
