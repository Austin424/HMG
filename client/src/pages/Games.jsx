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

    return(

        <div className="container" style={{backgroundColor:"#AF811C", height:"100%"}}>
            {games.map((game) => (
    <div className="hexagon" key={game.id} style={{ border: "5px brown solid", margin: "5px", height:"400px", width:"400px", clipPath:"polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%)"}}>
        <h1>{game.title}</h1>
        <img id={game.title} src={game.boxArt} alt={game.title} style={{height:"auto", width:"100%", objectFit:"cover"}}/>
        <h2 style={{textAlign:"center"}}>{game.developer}</h2>
        <h2 style={{textAlign:"center"}}>{game.publisher}</h2>
        <h3 style={{textAlign:"center"}}>{game.genre}</h3>
    </div>
    ))}
</div>

    )
}
export default Games