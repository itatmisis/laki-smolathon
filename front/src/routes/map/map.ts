import type { DomEventHandlerObject, LngLat, YMap, YMapListener } from "@yandex/ymaps3-types";
import Marker from "./Marker.svelte";
import type { IconKind } from "$lib";
import type { Feature } from "@yandex/ymaps3-types/packages/clusterer";
import { PlacesList } from "$lib/core/places";

const center: LngLat = [32.045287, 54.782635];
const zoom = 10;
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

    AddCallbacks(map);

    await initClusterer(map);
}

async function initClusterer(map: YMap) {
    const { YMapClusterer, clusterByGrid } = await ymaps3.import("@yandex/ymaps3-clusterer@0.0.1");

    const points: Feature[] = markers.map((marker, i) => ({
        type: "Feature",
        id: i.toString(),
        geometry: { coordinates: marker.location, type: "Point" },
        properties: {}
    }));

    const marker = (feature: Feature) =>
        new ymaps3.YMapMarker(
            { coordinates: feature.geometry.coordinates },
            createMarkerElement("heart")
        );

    const cluster = (coordinates: LngLat, features: Array<Feature>) =>
        new ymaps3.YMapMarker({ coordinates }, createMarkerElement(features.length));

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

    const clickCallback = (object: DomEventHandlerObject) => {
        if (object && object.type == "marker") {
            console.log(object.entity.element);
        }
    };

    const mapListener = new YMapListener({
        layer: 'any',
        onClick: clickCallback
    });

    return mapListener;
}

function createMarkerElement(content: IconKind | number): HTMLElement {
    const markerElement = document.createElement("div");
    new Marker({ target: markerElement, props: { kind: content } });
    return markerElement;
}

function AddCallbacks(map: YMap) {
    const { YMapListener } = ymaps3;

    const clickCallback = (object: DomEventHandlerObject) => {
        if (!object || object.type != "marker") {
            return;
        }
        console.log(object.entity);
        alert("Нажатие на маркер!")
    };

    const mapListener = new YMapListener({
        layer: "any",
        onClick: clickCallback
    });

    map.addChild(mapListener);
}
