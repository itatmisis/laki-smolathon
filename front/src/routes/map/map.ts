import type { DomEventHandlerObject, LngLat, YMap, YMapListener } from "@yandex/ymaps3-types";
import Marker from "./Marker.svelte";
import type { IconKind } from "$lib";
import type { Feature } from "@yandex/ymaps3-types/packages/clusterer";
import { place, PlacesList } from "$lib/core/places";
import PlaceDrawer from "$lib/PlaceDrawer/PlaceDrawer.svelte";

const center: LngLat = [32.045287, 54.782635];
const zoom = 13;
const markers = PlacesList();

export let map: YMap | undefined = undefined;

export async function InitMap(mapElem: HTMLElement) {
    if (map === undefined) {
        console.log("Awaiting...");
        await ymaps3.ready;
        console.log("Awaited!");
    }

    map = new ymaps3.YMap(mapElem, {
        location: { center, zoom }
    });

    const { YMapDefaultSchemeLayer, YMapDefaultFeaturesLayer } = ymaps3;

    map.addChild(new YMapDefaultSchemeLayer({}));
    map.addChild(new YMapDefaultFeaturesLayer({}));
    map.addChild(createCallbacks());

    await initClusterer(map);
}

async function initClusterer(map: YMap) {
    const { YMapClusterer, clusterByGrid } = await ymaps3.import("@yandex/ymaps3-clusterer@0.0.1");

    const points: Feature[] = [];
    for (const marker of await markers) {
        points.push({
            type: "Feature",
            id: marker.id.toFixed(0),
            geometry: { coordinates: marker.location, type: "Point" },
            properties: { "category": marker.category }
        });
    }

    const marker = (feature: Feature) => {
        let id = feature.id;
        let kind: IconKind = "heart";
        let icon = feature.properties!["category"] as string;

        const markerElement = document.createElement("div");
        new Marker({ target: markerElement, props: { id, kind, icon } });
        return new ymaps3.YMapMarker(
            {
                coordinates: feature.geometry.coordinates,
                properties: { id }
            },
            markerElement
        );
    }

    const cluster = (coordinates: LngLat, features: Array<Feature>) => {
        let id = features.map(f => f.id);
        let kind = features.length;
        let icon = "cluster";

        const markerElement = document.createElement("div");
        new Marker({ target: markerElement, props: { id, kind, icon } });
        return new ymaps3.YMapMarker(
            { coordinates, properties: { id } },
            markerElement
        );
    };

    const clusterer = new YMapClusterer({
        method: clusterByGrid({ gridSize: 64 }),
        features: points,
        marker,
        cluster
    });

    map.addChild(clusterer);
}

function createCallbacks(): YMapListener {
    const { YMapListener } = ymaps3;

    const clickCallback = async (object: DomEventHandlerObject) => {
        if (object && object.type == "marker") {
            let id = object.entity.properties?.id as string | string[] | undefined;
            if (typeof id == "string") {
                const target = document.createElement("div");
                document.body.appendChild(target);
                new PlaceDrawer({ target, props: { place: await place(Number(id)) } });
            } else if (typeof id == "object") {
                console.log(id);
            }
        }
    };

    const mapListener = new YMapListener({
        layer: 'any',
        onClick: clickCallback
    });

    return mapListener;
}
