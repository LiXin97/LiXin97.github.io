import { SITE } from "@config";
import { defineCollection, z } from "astro:content";

type PubEntry = {
  id: string;
  slug: string;
  body: string;
  collection: "pub"; // Ensure this matches the expected collection name
  data: {
    title: string;
    authors: {
      name: string;
      url: string;
    }[];
    published_year: number;
    published_place: string;
    bibtex: string;
    links: {
      name: string;
      url: string;
    }[];
    homepage: string;
    paper_id: string;
  };
};

const blog = defineCollection({
  type: "content",
  schema: ({ image }) =>
    z.object({
      author: z.string().default(SITE.author),
      pubDatetime: z.date(),
      modDatetime: z.date().optional().nullable(),
      title: z.string(),
      featured: z.boolean().optional(),
      draft: z.boolean().optional(),
      tags: z.array(z.string()).default(["others"]),
      ogImage: image()
        .refine(img => img.width >= 1200 && img.height >= 630, {
          message: "OpenGraph image must be at least 1200 X 630 pixels!",
        })
        .or(z.string())
        .optional(),
      description: z.string(),
      canonicalURL: z.string().optional(),
    }),
});

const pub = defineCollection({
  type: "content",
  schema: ({ image }) =>
    z.object({
      title: z.string(),
      authors: z.array(
        z.object({
          name: z.string(),
          url: z.string(),
        })
      ),
      published_year: z.number(),
      published_place: z.string(),
      bibtex: z.string(),
      links: z.array(
        z.object({
          name: z.string(),
          url: z.string(),
        })
      ),
      homepage: z.string(),
      paper_id: z.string(),
    }),
});

export const collections = { blog, pub };


// authors:
//   - name: Xin Li*
//     url: https://lixin.ai/
//   - name: Yijia He*
//     url: https://scholar.google.com/citations?user=_0lKGnkAAAAJ&hl=en
//   - name: Jinlong Lin
//     url: https://www.ss.pku.edu.cn/teacherteam/teacherlist/1652-%E6%9E%97%E9%87%91%E9%BE%99.html
//   - name: Xiao Liu
// published_place: IROS
// published_year: 2020
// paper_id: "u5HHmVD_uO8C"
// title: Leveraging Planar Regularities for Point Line Visual-Inertial Odometry
// slug: leveraging-planar-regularities-for-point-line-visual-inertial-odometry
// featured: true
// bibtex:
//   |-
//     @inproceedings{li2020leveraging,
//       title={Leveraging Planar Regularities for Point Line Visual-Inertial Odometry},
//       author={Li, Xin and He, Yijia and Lin, Jinlong and Liu, Xiao},
//       booktitle={2020 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)},
//       pages={10792--10798},
//       year={2020},
//       organization={IEEE}
//     }
// homepage: https://arxiv.org/abs/2004.11969
// links:
//   - name: PDF
//     url: https://arxiv.org/abs/2004.11969
//   - name: arXiv
//     url: https://arxiv.org/abs/2004.11969
//   - name: video
//     url: https://www.youtube.com/watch?v=V1KU6V49UKI
//   - name: code
//     url: https://github.com/LiXin97/Co-Planar-Parametrization-VIO