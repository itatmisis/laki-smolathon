import type { LngLat } from "@yandex/ymaps3-types";
import type { Filter } from "./filters";

export function getListOfPlaces(filter: Filter) {
    // TODO
}

export type Place = {
    name: string;
    description: string;
    category: Category;
    location: LngLat;
};

export type Category = (typeof Categories)[number];

const Categories = ["Музеи", "Храмы", "Соборы", "Памятники"] as const;

export function PlacesList(): Place[] {
    return [
        { name: "", category: "Музеи", description: "", location: [32.050440, 54.779149] },
        { name: "", category: "Музеи", description: "", location: [32.039652, 54.784326] },
        { name: "", category: "Музеи", description: "", location: [32.038918, 54.783035] },
        { name: "", category: "Музеи", description: "", location: [32.038919, 54.783035] },
        { name: "", category: "Музеи", description: "", location: [32.043420, 54.773421] },
        { name: "", category: "Музеи", description: "", location: [32.041720, 54.781649] },
        { name: "", category: "Музеи", description: "", location: [32.047657, 54.772328] },
        { name: "", category: "Музеи", description: "", location: [32.047674, 54.782107] },
        { name: "", category: "Музеи", description: "", location: [32.054602, 54.788829] },
        { name: "", category: "Музеи", description: "", location: [32.020403, 54.791456] },
        { name: "", category: "Музеи", description: "", location: [32.053246, 54.773294] },
        { name: "", category: "Музеи", description: "", location: [32.053128, 54.778505] },
        { name: "", category: "Музеи", description: "", location: [32.044505, 54.777941] },
        { name: "", category: "Музеи", description: "", location: [32.059094, 54.780337] },
        { name: "", category: "Музеи", description: "", location: [32.053081, 54.778505] },
        { name: "", category: "Музеи", description: "", location: [32.059972, 54.781137] },
        { name: "", category: "Музеи", description: "", location: [32.046122, 54.780461] },
        { name: "", category: "Музеи", description: "", location: [32.049970, 54.782356] }
    ]
}
