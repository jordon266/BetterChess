


async function getGames(response, setGame,games,color) {
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

  export {getGames}