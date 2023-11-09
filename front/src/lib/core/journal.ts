import type { Place } from "./places";

export type Journal = {
    entries: Place;
};

export type JournalEntry = {
    place: Place;
    photos: string[];
};
