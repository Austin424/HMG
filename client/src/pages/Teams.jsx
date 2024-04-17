import { useState, useEffect} from "react";
import TeamPostButtonForm from "../components/TeamPostButtoForm";

function Teams() {

    const [posts, setPosts] = useState([]);

    useEffect(() => {
        fetchPosts();
    }, []);

    const fetchPosts = async () => {
        try {
            const response = await fetch('/api/team_posts');
            if (response.ok) {
                const data = await response.json();
                setPosts(data);
            } else {
                console.error('Failed to fetch team posts');
            }
        } catch (error) {
            console.error('Failed to fetch team posts:', error);
        }
    };

    return(
        <>
        <TeamPostButtonForm/>
        <div>
            <h1 style={{textAlign:"center", textDecoration:"underline", color:"white"}}>Team Posts</h1>
            {posts.map(post => (
                <div style={{border:"1px solid white", width:"300px", height:"200px", marginBottom:"5px",
                
                }} key={post.id}>
                    <p style={{color:"white", textAlign:"center"}}>Game: {post.game_id}</p>
                    <p style={{color: "white", textAlign:"center"}}> Username: {post.creator_id}</p>
                    <p style={{color: "white", textAlign:"center"}}> Role: {post.role}</p>
                    <p style={{color: "white", textAlign:"center"}}>Avaible Spots: {post.open_spots}</p>

                </div>
            ))}
        </div>
        
        </>
    )
}

export default Teams