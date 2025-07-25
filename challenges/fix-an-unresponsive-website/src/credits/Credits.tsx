import React, { useState, useEffect, JSX } from "react";

const Credits = () => {
    const credits = [
        { name: "John", role: "developer" },
        { name: "Jane", role: "developer" },
        { name: "Jack", role: "developer" },
        { name: "Jill", role: "developer" },
        { name: "James", role: "developer" },
        { name: "Jenny", role: "developer" },
        { name: "Jade", role: "developer" },
        { name: "Jasmine", role: "developer" },
        { name: "Jasper", role: "developer" },
        { name: "Jared", role: "developer" },
        { name: "Jocelyn", role: "developer" },
        { name: "Jude", role: "developer" },
        { name: "Jules", role: "developer" },
        { name: "Julian", role: "developer" },
        { name: "Julia", role: "developer" },
    ];

    const [data, setData] = useState<JSX.Element[]>([]);
    const [currentIndex, setCurrentIndex] = useState(0);

    useEffect(() => {
        if (currentIndex < credits.length) {
            const timeout = setTimeout(() => {
                setData((prevData) => [
                    ...prevData,
                    <p key={currentIndex}>
                        {credits[currentIndex].name} - {credits[currentIndex].role}
                    </p>,
                ]);
                setCurrentIndex((prevIndex) => prevIndex + 1);
            }, 100); // Simulate the delay for each credit
            return () => clearTimeout(timeout);
        }
    }, [currentIndex, credits]);

    return (
        <div>
            This app was written by:
            {data}
        </div>
    );
};

export default Credits;