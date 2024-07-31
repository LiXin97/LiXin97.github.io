import { slugifyStr } from "@utils/slugify";
import Datetime from "./Datetime";
import type { CollectionEntry } from "astro:content";
import React, { useState } from 'react';


export interface Props {
    href?: string;
    frontmatter: CollectionEntry<"pub">["data"];
    secHeading?: boolean;
}

export default function PubCard({ href, frontmatter, secHeading = true }: Props) {
    const { title, authors, published_year, published_place, bibtex, links, homepage, paper_id, og_image } = frontmatter;

    const headerProps = {
        style: { viewTransitionName: slugifyStr(title) },
        className: "text-lg font-medium decoration-dashed hover:underline",
    };

    let [showBibtex, setShowBibtex] = useState(false);

    let toggleBibtex = () => {
        setShowBibtex(!showBibtex);
    };

    const show_google_citations = () => {
        let citation_url = "https://img.shields.io/endpoint?logo=Google%20Scholar&url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2FLiXin97%2Flixin97.github.io@google-scholar-stats%2Fgs_data_Hxf8sNkAAAAJ:" + paper_id + ".json&labelColor=f6f6f6&color=9cf&style=flat&label=citations";
        return (
            // <p>{citation_url}</p>
            <a href="https://scholar.google.com/citations?user=Hxf8sNkAAAAJ">
                <img src={citation_url} alt="Google Scholar Citations" ></img>
            </a>
        );
    }

    return (

        <div>
            {/* create struct data */
                <div itemType="http://schema.org/ScholarlyArticle">
                    <meta itemProp="headline" content={title} />
                    <meta itemProp="author" content={authors.map((author) => author.name).join(", ")} />
                    <meta itemProp="datePublished" content={published_year.toString()} />
                    <meta itemProp="publisher" content={published_place} />
                    <meta itemProp="image" content={og_image} />
                    <meta itemProp="url" content={homepage} />
                </div>
            }

            <table style={{ width: '100%', margin: 'auto' }} border={1}>

                <tr>
                    <td style={{ width: '20%' }}>
                        <img
                            src={og_image}
                            alt={title}
                        />
                    </td>

                    <td>
                        <li className="my-6">
                            <a
                                href={homepage}
                                className="inline-block text-lg font-medium text-skin-accent decoration-dashed underline-offset-4 focus-visible:no-underline focus-visible:underline-offset-0"
                            >
                                {secHeading ? (
                                    <h2 {...headerProps}>{title}</h2>
                                ) : (
                                    <h3 {...headerProps}>{title}</h3>
                                )}
                            </a>

                            {
                                authors.map((author, index) => (
                                    <span key={index} className="text-sm font-light">
                                        {index === 0 ? "Authors: " : ""}
                                        {
                                            // if author.name == "Xin Li", bold the name
                                            author.url ? (
                                                <a href={author.url} className="decoration-dashed hover:underline underline">
                                                    {author.name}
                                                </a>
                                            ) : author.name
                                        }
                                        {index === authors.length - 1 ? "" : ", "}
                                    </span>
                                ))
                            }

                            <p className="text-sm font-light">Published in: {published_place}, {published_year.toString()}</p>
                            {
                                // homepage ? (
                                //     <p className="text-sm font-light">Homepage: <a href={homepage} className="decoration-dashed hover:underline underline">{homepage}</a></p>
                                // ) : ""
                            }
                            {
                                links.map((link, index) => (
                                    <span key={index} className="text-sm font-light">
                                        {index === 0 ? "Links: " : ""}
                                        {
                                            link.url ? (
                                                <a href={link.url} className="decoration-dashed hover:underline underline">
                                                    {link.name}
                                                </a>
                                            ) : link.name
                                        }
                                        {index === links.length - 1 ? "" : " / "}
                                    </span>
                                ))
                            }

                            {
                                // show 
                                show_google_citations()
                            }

                            {
                                // <div className="text-sm font-light">
                                //     <button onClick={toggleBibtex} className="underline">Show BibTeX</button>
                                // </div>
                            }

                            {
                                showBibtex && (
                                    <div className="modal-content">
                                        <button onClick={() => setShowBibtex(false)} style={{ float: 'right' }}>Close</button>
                                        <pre>{bibtex}</pre>
                                    </div>
                                )
                            }
                        </li>
                    </td>
                </tr>
            </table >

        </div >
    );
}