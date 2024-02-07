import {Component, OnInit} from '@angular/core';
import {ActivatedRoute, Router} from "@angular/router";
import {DocumentRetrievingService} from "../../services/document-retrieving.service";
import {Article} from "../../dto/article";

@Component({
  selector: 'app-search-result',
  templateUrl: './search-result.component.html',
  styleUrl: './search-result.component.css'
})
export class SearchResultComponent implements OnInit {
  documents?: Article[] = [];
  query: string = '';
  algorithm: string = '';

  ngOnInit() {
    this.route.params.subscribe(params => {
      this.query = params['data'];
      this.algorithm = params['algorithm'];
    });

    this.documentRetrievingService.getBestDocumentCandidates(this.query, this.algorithm).subscribe(
      (result: Article[]) => {
        this.documents = result;
      },
      (error) => {
        // console.error('Error:', error);
      }
    );
  }

  constructor(private route: ActivatedRoute,
              private documentRetrievingService: DocumentRetrievingService,
              private router: Router) {}

  onTitleClick(doc: Article) {
      this.router.navigate(['/document', doc.doc_id]);
  }
}
