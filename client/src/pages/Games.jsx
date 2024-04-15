import { useEffect, useState } from "react"

import'./game.css'

function Games() {

    const [games, setGames] = useState([]);

    useEffect(() => {
        async function fetchGames() {
            try {
                const response = await fetch("http://localhost:3000/games");
                const data = await response.json();
                setGames(data);
            }
            catch (error) {
                console.error("Error fecthing data", error);
                throw error;
            }
        }
        fetchGames();
    }, []);

    console.log(games)
    return(

        <div className="container" style={{height:"100%"}}>
            {games.map((game) => (
    <div key={game.id} style={{ border: "5px brown solid", margin: "5px"}}>
        <h1>{game.name}</h1>
        <img id={game.name} src={game.boxart} alt={game.name} style={{height:"auto", width:"100%", objectFit:"cover"}}/>
        <h2 style={{textAlign:"center"}}>{game.developer}</h2>
        <h2 style={{textAlign:"center"}}>{game.publisher}</h2>
        <h3 style={{textAlign:"center"}}>{game.genre}</h3>
    </div>
    ))}
</div>

    )
}
export default Games