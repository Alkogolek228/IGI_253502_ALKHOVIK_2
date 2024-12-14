import React, { useContext, useEffect } from 'react';
import styled from 'styled-components';
import { PageContainer, Text } from '../../components/GlobalStyles/PageStyles';
import { GlobalContext } from '../../utils/Context';

const AboutContainer = styled(PageContainer)`
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 20px;
    background-color: #f9f9f9;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
`;

const Title = styled.h1`
    font-size: 2.5em;
    color: #333;
    margin-bottom: 20px;
`;

const Paragraph = styled.p`
    font-size: 1.2em;
    color: #666;
    line-height: 1.6;
    margin-bottom: 20px;
    text-align: center;
    max-width: 800px;
`;

const About = () => {
    const { setPage } = useContext(GlobalContext);

    useEffect(() => {
        setPage("About");
    }, []);

    return (
        <AboutContainer>
            <Title>About Us</Title>
            <Paragraph>
                Welcome to our Hotel Booking App. We provide the best hotel booking experience with a wide range of hotels to choose from.
            </Paragraph>
            <Paragraph>
                Our mission is to make hotel booking easy and convenient for everyone. Whether you are traveling for business or leisure, we have the perfect hotel for you.
            </Paragraph>
            <Paragraph>
                Thank you for choosing our service. We hope you have a great experience!
            </Paragraph>
        </AboutContainer>
    );
};

export default About;