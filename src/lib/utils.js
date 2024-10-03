// Import the local verbal reasoning questions JSON file
import verbalQuestions from '../assets/questions.json'; // Corrected path from 'assests' to 'assets'

/**
 * Shuffles array in place. ES6 version
 * @param {Array} a items An array containing the items.
 * 
 * Reference: https://stackoverflow.com/questions/6274339/how-can-i-shuffle-an-array
 */
export function shuffle(a) {
    for (let i = a.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [a[i], a[j]] = [a[j], a[i]];
    }
    return a;
}

export function getToday() {
    return (new Date()).toISOString().split('T')[0];
}

// Fetch quiz questions from a local JSON file
export async function getRemoteData() {
    try {
        // Fetch the questions from the imported JSON file
        return verbalQuestions; // Return the imported questions directly
    } catch (error) {
        console.error('Error loading data:', error);
        throw error; // Rethrow the error to handle it in the calling function
    }
}
