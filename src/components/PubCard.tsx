import { slugifyStr } from "@utils/slugify";
import React, { useState } from 'react';

interface Author {
    name: string;
    url?: string;
}

interface PubData {
    title: string;
    authors: Author[];
    published_year: number;
    published_place: string;
    og_image: string;
    homepage: string;
    bibtex: string;
    links: { name: string; url?: string }[];
    paper_id: string;
}

interface StructuredMetaDataProps {
    title: string;
    authors: Author[];
    published_year: number;
    published_place: string;
    og_image: string;
    homepage: string;
}

const StructuredMetaData = ({ title, authors, published_year, published_place, og_image, homepage }: StructuredMetaDataProps) => {
    const structuredData = {
        "@context": "http://schema.org",
        "@type": "ScholarlyArticle",
        "headline": title,
        "author": authors.map((author: { name: string; url?: string }, index: number, array: Author[]) => ({
            "@type": "Person",
            "name": author.name.endsWith("*") ? author.name.slice(0, -1) : author.name,
            "url": author.url || undefined  // Only include the URL if it exists
        })),
        "datePublished": published_year.toString(),
        "publisher": published_place,
        "image": og_image,
        "url": homepage
    };

    return (
        <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(structuredData) }}
      />
    );
}

interface PubCardProps {
    href?: string;
    frontmatter: PubData;
    secHeading?: boolean;
}

export default function PubCard({ href, frontmatter, secHeading = true }: PubCardProps) {
    const { title, authors, published_year, published_place, bibtex, links, homepage, paper_id, og_image } = frontmatter;
    const [showBibtex, setShowBibtex] = useState(false);

    const headerProps = {
        style: { viewTransitionName: slugifyStr(title) },
        className: "text-lg font-medium decoration-dashed hover:underline",
    };

    let toggleBibtex = () => {
        setShowBibtex(!showBibtex);
    };

    const showGoogleCitations = () => {
        let citation_url = "https://img.shields.io/endpoint?logo=Google%20Scholar&url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2FLiXin97%2Flixin97.github.io@google-scholar-stats%2Fgs_data_Hxf8sNkAAAAJ:" + paper_id + ".json&labelColor=f6f6f6&color=9cf&style=flat&label=citations";
        return (
            // <p>{citation_url}</p>
            // <a href="https://scholar.google.com/citations?user=Hxf8sNkAAAAJ">
            //     <img src={citation_url} alt="Google Scholar Citations" ></img>
            // </a>
            // <a href="default.asp"><img src="smiley.gif" alt="HTML tutorial" style="width:42px;height:42px;"></a>

            <div>
                <a href="https://scholar.google.com/citations?user=Hxf8sNkAAAAJ" className="inline-block text-lg font-medium text-skin-accent decoration-dashed underline-offset-4 focus-visible:no-underline focus-visible:underline-offset-0">
                    <img src={citation_url} alt="Google Scholar Citations"></img>
                </a>
            </div>
            
        );
    }

    const copyToClipboard = () => {
        navigator.clipboard.writeText(bibtex).then(() => {
          alert('BibTeX entry copied to clipboard!');
        }, (err) => {
          console.error('Could not copy text: ', err);
        });
    };

    return (

        <div>
            <StructuredMetaData title={title} authors={authors} published_year={published_year} published_place={published_place} og_image={og_image} homepage={homepage} />

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
                            {showGoogleCitations()}
                        </li>
                    </td>
                </tr>
            </table >

        </div >
    );
}