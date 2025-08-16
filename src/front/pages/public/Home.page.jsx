import React from 'react';
import './public.css';
import { Link } from 'react-router-dom';
import { Navbar } from '../../components/Navbar';
import { Footer } from '../../components/Footer';


export default function HomePage() {

    return (
        <>
            <Navbar></Navbar>
            <h1>hola home</h1>
            <Link to={"/login"}>
                <button>Login</button>
            </Link>

            <Footer></Footer>
        </>
    )
}