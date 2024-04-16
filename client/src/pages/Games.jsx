import { useEffect, useState } from "react"

import'./game.css'

function Games() {

    const [games, setGames] = useState([]);

    useEffect(() => {
        async function fetchGames() {
            try {
                const response = await fetch("/api/games");
                const data = await response.json();
                setGames(data);
            }
            catch (error) {
                console.error("Error fetching data", error);
                throw error;
            }
        }
        fetchGames();
    }, []);

    console.log(games)
    return(

        <div className="container" style={{height:"100%", display:"grid", gridTemplateColumns: "repeat(3, 1fr)", overflow:"hidden"}}>
            {games.map((game) => (
    <div key={game.id} style={{ border: "1px white solid", margin: "5px", maxWidth:"100%", backgroundColor:"grey"}}>
        <h1 style={{textAlign:"center"}}>{game.name}</h1>
        <img id={game.name} src={game.boxart} alt={game.name} style={{height:"400px", width:"100%", objectFit:"cover"}}/>
        <h2 style={{textAlign:"center"}}>{game.developer}</h2>
        <h2 style={{textAlign:"center"}}>{game.publisher}</h2>
        <h3 style={{textAlign:"center"}}>{game.genre}</h3>
    </div>
    ))}
</div>

    )
}
export default Games