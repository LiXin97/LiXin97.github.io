import type { CollectionEntry } from "astro:content";

const getSortedPubs = (pubs: CollectionEntry<"pubs">[]) => {
  return pubs
    .sort(
      (a, b) =>
        Math.floor(
          new Date(b.data.published_year)
        ) -
        Math.floor(
          new Date(a.data.published_year)
        )
    );
};

export default getSortedPubs;
