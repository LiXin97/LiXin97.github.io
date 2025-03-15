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
    homepage: string;
    bibtex: string;
    links: { name: string; url?: string }[];
    paper_id: string;
    tags: string[];
}

interface StructuredMetaDataProps {
    title: string;
    authors: Author[];
    published_year: number;
    published_place: string;
    homepage: string;
    tags?: string[];
}

const StructuredMetaData = ({ title, authors, published_year, published_place, homepage, tags }: StructuredMetaDataProps) => {
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
    const { title, authors, published_year, published_place, bibtex, links, homepage, paper_id, tags } = frontmatter;
    const [showBibtex, setShowBibtex] = useState(false);

    const headerProps = {
        style: { viewTransitionName: slugifyStr(title) },
        className: "text-base font-medium decoration-dashed hover:underline",
    };

    let toggleBibtex = () => {
        setShowBibtex(!showBibtex);
    };

    const showGoogleCitations = () => {
        if (paper_id == "") return null;
        let citation_url = "https://img.shields.io/endpoint?logo=Google%20Scholar&url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2FLiXin97%2Flixin97.github.io@google-scholar-stats%2Fgs_data_Hxf8sNkAAAAJ:" + paper_id + ".json&labelColor=f6f6f6&color=9cf&style=flat&label=citations";
        return (
            <a href="https://scholar.google.com/citations?user=Hxf8sNkAAAAJ" className="inline-block align-middle">
                <img src={citation_url} alt="Google Scholar Citations" />
            </a>
        );
    }

    const copyToClipboard = () => {
        navigator.clipboard.writeText(bibtex).then(() => {
            alert('BibTeX entry copied to clipboard!');
        }).catch((err) => {
            console.error('Could not copy text: ', err);
        });
    };

    const renderAuthorName = (author: Author) => {
        const isXinLi = author.name === "Xin Li" || author.name === "Xin Li*";
        const displayName = (
            isXinLi ? <b>{author.name}</b> : author.name
        );

        return author.url ? (
            <a href={author.url} className="decoration-dashed hover:underline">
                {displayName}
            </a>
        ) : displayName;
    };

    // Get a color based on the tag name
    const getTagColor = (tag: string) => {
        // Simple hash function to get consistent colors for tags
        const hash = tag.split('').reduce((acc, char) => {
            return char.charCodeAt(0) + ((acc << 5) - acc);
        }, 0);
        
        // Convert to a color in the accent palette with different opacity levels
        return `var(--color-accent), ${Math.abs(hash) % 20 + 10}%`;
    };

    return (
        <div>
            <StructuredMetaData title={title} authors={authors} published_year={published_year} published_place={published_place} homepage={homepage} />

            <li className="my-4">
                <a
                    href={homepage}
                    className="inline-block text-lg font-medium hover:text-skin-accent decoration-dashed underline-offset-4 focus-visible:no-underline"
                >
                    <h3 {...headerProps}>{title}</h3>
                </a>

                <div className="text-sm mt-1 mb-1">
                    {authors.map((author, index) => (
                        <span key={index}>
                            {renderAuthorName(author)}
                            {index === authors.length - 1 ? '.' : ', '}
                        </span>
                    ))}
                </div>

                <p className="text-sm font-light">{published_place}, {published_year.toString()}.</p>
                
                {/* Tags display */}
                {tags && tags.length > 0 && (
                    <div className="flex flex-wrap gap-1 mt-1 mb-1">
                        {tags.map(tag => (
                            <a 
                                key={tag}
                                href={`/pubs/tags/${slugifyStr(tag)}/`}
                                className="inline-flex items-center px-2 py-0.5 rounded-md text-xs font-medium bg-skin-accent/10 text-skin-accent hover:bg-skin-accent/20 transition-colors"
                            >
                                <svg 
                                    className="w-3 h-3 mr-1" 
                                    fill="currentColor" 
                                    viewBox="0 0 20 20"
                                >
                                    <path fillRule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clipRule="evenodd" />
                                </svg>
                                {tag}
                            </a>
                        ))}
                    </div>
                )}

                <div className="flex flex-wrap items-center gap-1 mt-1">
                    {links.map((link, index) => (
                        <span key={index} className="text-sm font-light">
                            {
                                link.url ? (
                                    <a href={link.url} className="hover:underline hover:text-skin-accent  decoration-dashed underline-offset-4 focus-visible:no-underline focus-visible:underline-offset-0">
                                        {link.name}
                                    </a>
                                ) : link.name
                            }
                            {index === links.length - 1 ? <span> / {showGoogleCitations()} </span> : " / "}
                        </span>
                    ))}
                    <button 
                        onClick={toggleBibtex}
                        className="inline-flex items-center text-sm font-light hover:text-skin-accent transition-colors duration-200"
                    >
                        <svg 
                            className="w-4 h-4 mr-1" 
                            fill="none" 
                            stroke="currentColor" 
                            viewBox="0 0 24 24"
                        >
                            <path 
                                strokeLinecap="round" 
                                strokeLinejoin="round" 
                                strokeWidth={2} 
                                d={showBibtex ? "M19 9l-7 7-7-7" : "M9 5l7 7-7 7"}
                            />
                        </svg>
                        BibTeX
                    </button>
                </div>
                {showBibtex && (
                    <div className="mt-3 p-4 bg-skin-card rounded-lg border border-skin-line shadow-sm transition-all duration-200 ease-in-out">
                        <pre className="text-sm overflow-x-auto font-mono bg-skin-fill p-3 rounded border border-skin-line text-skin-base">
                            {bibtex}
                        </pre>
                        <div className="mt-2 flex justify-end">
                            <button 
                                onClick={copyToClipboard}
                                className="inline-flex items-center px-3 py-1 text-sm font-medium text-skin-base bg-skin-card border border-skin-line rounded-md hover:bg-skin-card hover:text-skin-accent transition-colors duration-200"
                            >
                                <svg 
                                    className="w-4 h-4 mr-1" 
                                    fill="none" 
                                    stroke="currentColor" 
                                    viewBox="0 0 24 24"
                                >
                                    <path 
                                        strokeLinecap="round" 
                                        strokeLinejoin="round" 
                                        strokeWidth={2} 
                                        d="M8 5H6a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2v-1M8 5a2 2 0 002 2h2a2 2 0 002-2M8 5a2 2 0 012-2h2a2 2 0 012 2m0 0h2a2 2 0 012 2v3m2 4H10m0 0l3-3m-3 3l3 3"
                                    />
                                </svg>
                                Copy
                            </button>
                        </div>
                    </div>
                )}
            </li>
        </div>
    );
}
