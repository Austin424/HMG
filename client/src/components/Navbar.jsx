import { NavLink } from 'react-router-dom';
import { GiTreeBeehive, GiBee } from 'react-icons/gi';
import { CgGames } from 'react-icons/cg';

function Navbar() {
    return (
        <header className="header" style={{ height: "100px", color: "white", alignItems: "center", display: "flex", justifyContent: "center", padding: "10px 20px", borderBottom: "1px solid white" }}>
        <nav>
            <ul style={{ listStyleType: "none", padding: 0, display: "flex", alignItems: "center" }}>
                <li style={{ marginRight: "50px", fontSize: "30px", display: "flex", alignItems: "center" }}>
                    <GiTreeBeehive style={{ marginRight: "5px" }} />
                    <NavLink to="/">Home</NavLink>
                </li>
                <li style={{ marginRight: "50px", fontSize: "30px", display: "flex", alignItems: "center" }}>
                    <CgGames style={{ marginRight: "5px" }} />
                    <NavLink to="">Games</NavLink>
                </li>
                <li style={{ marginRight: "50px", fontSize: "30px", display: "flex", alignItems: "center" }}>
                    <GiBee style={{ marginRight: "5px" }} />
                    <NavLink to="">Teams</NavLink>
                </li>
            </ul>
        </nav>
        <button style={{clipPath:"polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%)",backgroundColor:"yellow",color:"black", height:"100px", width:"100px", marginLeft: "auto"}}>Sign Up</button>
        <button style={{clipPath:"polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%)",backgroundColor:"yellow",color:"black", height:"100px", width:"100px", marginLeft: "20px"}}>Login</button>
    </header>
    
    );
}

export default Navbar;
