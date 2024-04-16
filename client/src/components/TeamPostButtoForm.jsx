import React, { useState } from 'react';

const  TeamPostButtonForm = () => {
    const [isOpen, setIsOpen] = useState(false);

    const toggleForm = () => {
    setIsOpen(!isOpen);
    };

    const handleSubmit = (event) => {
    // Handle form submission here
    event.preventDefault();
    // Example: Reset form state
    setIsOpen(false);
    };

    return (
    <div>
        <button style={{alignItems:"center"}} onClick={toggleForm}>
            {isOpen ? 'Close Form' : 'Create A Post'}
        </button>
        {isOpen && (
        <form onSubmit={handleSubmit}>
          {/* Your form fields go here */}
            <label>
            Name:
            <input type="text" name="name" />
            </label>
            <label>
            Email:
            <input type="email" name="email" />
            </label>
          {/* Add more form fields as needed */}
            <button type="submit">Submit</button>
        </form>
        )}
    </div>
    );
};

export default  TeamPostButtonForm;
