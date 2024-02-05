import {Component, OnInit} from '@angular/core';
import {ActivatedRoute} from "@angular/router";
import {DocumentRetrievingService} from "../../services/document-retrieving.service";

@Component({
  selector: 'app-present-document',
  templateUrl: './present-document.component.html',
  styleUrl: './present-document.component.css'
})
export class PresentDocumentComponent implements OnInit{
  id: string = '';
  content: string = '';

  constructor(private route: ActivatedRoute,
              private documentRetrievingService: DocumentRetrievingService) {}

  ngOnInit(): void {
    this.route.params.subscribe((params) => {
      this.id = params['id'];
    });

    this.documentRetrievingService.getSingleDocument(this.id).subscribe(
      (result: string) => {
        this.content = result;
        console.log(result);
      },
      (error) => {
        // console.error('Error:', error);
      }
    );
  }
}
