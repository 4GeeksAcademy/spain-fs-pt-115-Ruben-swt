import React from 'react';
import './sinUp.css';

export default function SinUpPage() {

    return (
        <>
            
                <form className="form">
                    <input type="text" className="input" placeholder="Enter your name" />
                    <input type="text" className="input" placeholder="Enter your email" />
                    <input type="password" className="input" placeholder="*********" />
                    <button>Submit</button>
                </form>
           
        </>
    )
}