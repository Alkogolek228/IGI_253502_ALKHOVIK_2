import React, { useEffect } from "react";
import { toast, ToastContainer } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";
import styled from "styled-components";

const JokeContainer = styled.div`
    text-align: center;
    margin-top: 20px;
`;

const Joke = () => {
    const fetchApi = () => {
        fetch("https://sv443.net/jokeapi/v2/joke/Programming?type=single")
            .then((res) => res.json())
            .then((data) => {
                toast(data.joke);
            });
    };

    useEffect(() => {
        fetchApi();
    }, []);

    return (
        <JokeContainer>
            <ToastContainer />
        </JokeContainer>
    );
}

export default Joke;