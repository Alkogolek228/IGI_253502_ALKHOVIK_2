import React, { useState, useEffect } from 'react';
import styled from 'styled-components';
import { getCurrentDateInUserTimezone, getCurrentDateInUTC, formatDateInUserTimezone, formatDateInUTC } from '../../utils/utilFunctions';

const TimeContainer = styled.div`
    position: fixed;
    bottom: 20px;
    left: 20px;
    min-width: 200px;
    max-width: 300px;
    padding: 10px;
    background-color: #f0f0f0;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    cursor: pointer;
`;

const TimeItem = styled.p`
    font-size: 14px;
    color: #333;
    margin: 5px 0;
    text-align: center;
`;

const ToggleButton = styled.button`
    background: none;
    border: none;
    color: #007bff;
    cursor: pointer;
    font-size: 14px;
    margin-top: 10px;
`;

const TimeComponent = ({ data }) => {
    const userTimezone = Intl.DateTimeFormat().resolvedOptions().timeZone;
    const [currentTime, setCurrentTime] = useState({
        userTime: getCurrentDateInUserTimezone(userTimezone),
        utcTime: getCurrentDateInUTC()
    });
    const [isExpanded, setIsExpanded] = useState(false);

    useEffect(() => {
        const intervalId = setInterval(() => {
            setCurrentTime({
                userTime: getCurrentDateInUserTimezone(userTimezone),
                utcTime: getCurrentDateInUTC()
            });
        }, 1000);

        return () => clearInterval(intervalId);
    }, [userTimezone]);

    const toggleExpand = () => {
        setIsExpanded(!isExpanded);
    };

    return (
        <TimeContainer onClick={toggleExpand}>
             <TimeItem>User's timezone: {userTimezone}</TimeItem>
            <TimeItem>Current date in user's timezone: {currentTime.userTime}</TimeItem>
            <TimeItem>Current date in UTC: {currentTime.utcTime}</TimeItem>
            {isExpanded && data.map(item => (
                <div key={item.id}>
                    <TimeItem>Date of adding/updating in user's timezone: {formatDateInUserTimezone(item.date, userTimezone)}</TimeItem>
                    <TimeItem>Date of adding/updating in UTC: {formatDateInUTC(item.date)}</TimeItem>
                </div>
            ))}
            <ToggleButton>{isExpanded ? 'Wrap' : 'Unwrap'}</ToggleButton>
        </TimeContainer>
    );
}

export default TimeComponent;