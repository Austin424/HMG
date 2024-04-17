import React, { useEffect, useState } from 'react';

const TeamPostButtonForm = () => {
    const [isOpen, setIsOpen] = useState(false);
    const [formData, setFormData] = useState({
        username: '',
        creator_id: '',
        role: '',
        open_spots: 0
    });

    const toggleForm = () => {
        setIsOpen(!isOpen);
    };

    const handleChange = (event) => {
        const { name, value } = event.target;
        setFormData({
            ...formData,
            [name]: value
        });
    };

    const handleSubmit = async (event) => {
        event.preventDefault();
        
        try {
            const response = await fetch('/api/team_posts', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(formData)
            });

            if (response.ok) {
                //clears form data after success
                setFormData({
                    username: '',
                    creator_id: '',
                    role: '',
                    open_spots: 0
                });
                setIsOpen(false);
                
            } else {
                
                console.error('Failed to add team post');
                
            }
        } catch (error) {
            console.error('Failed to add team post:', error);
            
        }
    };

    return (
        <div>
            <button style={{ display: "flex", alignItems: "center", justifyContent: "center" }} onClick={toggleForm}>
                {isOpen ? 'Close Form' : 'Create A Post'}
            </button>
            {isOpen && (
                <form style={{border:"1px solid whtie", width: "300px",display: "flex", flexDirection: "column" }} onSubmit={handleSubmit}>
                    <label style={{color:"white"}}>
                        Username:
                        <input type="text" name="username" value={formData.username} onChange={handleChange} />
                    </label>
                    <label style={{color:"white"}}>
                        Creator ID#:
                        <input type="text" name="creator_id" value={formData.creator_id} onChange={handleChange} />
                    </label>
                    <label style={{color:"white"}}>
                        Role:
                        <input type="text" name='role' value={formData.role} onChange={handleChange} />
                    </label>
                    <label style={{color:"white"}}>
                        Number of Spots Left:
                        <input style={{width:"40px"}} type="number" name='spots_left' value={formData.open_spots} onChange={handleChange} />
                    </label>
                    <button type="submit">Make Post</button>
                </form>
            )}
        </div>
    );
};

export default TeamPostButtonForm;






// import React, { useEffect, useState } from 'react';


// const  TeamPostButtonForm = () => {
//     const [isOpen, setIsOpen] = useState(false);

    

//     const [game, setGame] = useState([])
//     const [creator, setCreator] = useState("")
//     const [role, setRole] = useState("")
//     const [openSpots, setOpenSpots] = useState(0)


    

//     const toggleForm = () => {
//     setIsOpen(!isOpen);
//     };

//     const handleSubmit = (event) => {
//     // Handle form submission here
//     event.preventDefault();

//     setIsOpen(false);
//     };

//     return (
//     <div>
//         <button style={{display:"flex",alignItems:"center", justifyContent:"center"}} onClick={toggleForm}>
//             {isOpen ? 'Close Form' : 'Create A Post'}
//         </button>
//         {isOpen && (
//         <form style={{width:"200px",backgroundColor:"white", display:"flex", flexDirection:"column"}} onSubmit={handleSubmit}>
//             <label>
//             Username:
//             <input type="text" name="username" />
//             </label>
//             <label>
//             Creator ID#:
//             <input type="text" name="creator_id" />
//             </label>
//             <label>
//             Role:
//             <input type="text" name='role' />
//             </label>
//             <label>
//             Number of Spots Left:
//             <input type="number" name='spots_left' />
//             </label>
//             <button type="submit">Submit</button>
//         </form>
//         )}
//     </div>
//     );
// };

// export default  TeamPostButtonForm;
