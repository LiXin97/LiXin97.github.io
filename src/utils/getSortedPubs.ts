import type { CollectionEntry } from "astro:content";

const getSortedPubs = (pubs: CollectionEntry<"pub">[]) => {
  return pubs
    .sort(
      (a, b) =>
        Math.floor(
          b.data.published_year
        ) -
        Math.floor(
          a.data.published_year
        )
    );
};

export default getSortedPubs;
